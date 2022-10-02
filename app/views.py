from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile, Programming, Work, Education, Software, Programming
from .forms import ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


class IndexView(View):
    """
    トップページのview
    """
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        work_data = Work.objects.all().order_by('-id')

        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data,
        })
    
class DetailView(View):
    """
    作品詳細ページのビュー
    """
    def get(self, request, *args, **kwargs):
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/detail.html', {
            'work_data': work_data
        })

class AboutView(View):
    """
    プロフィール
    """

    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        education_data = Education.objects.order_by('period')
        software_data = Software.objects.order_by('-id')
        technical_data = Programming.objects.order_by('-id')
        return render(request, 'app/about.html', {
            'profile_data': profile_data,
            'education_data': education_data,
            'software_data': software_data,
            'technical_data': technical_data,
        })


class ContactView(View):
    """
    お問い合わせページ
    """
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        return render(request, 'app/contact.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        # フォームが妥当であれば，ホームページにリダイレクト
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            contact = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。

                {name} 様

                お問い合わせありがとうございます。
                以下の内容でお問い合わせを受付いたしました。
                内容を確認させていただき、ご返信させていただきますので、少々お待ちください。

                ---------------
                ◆お名前
                {name}

                ◆メールアドレス
                {email}

                ◆メッセージ
                {message}
                ---------------

                ※This email is an automatic reply from the system.

                Dear {name}

                Thank you for your inquiry.
                We have received inquiries with the above contents.
                We will check the contents and reply to you, so please be patient.
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )
            to_list = [email]
            #自分のメールアドレスをBccに追加
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=contact, to=to_list, bcc=bcc_list)
                #メールを送信
                message.send()
            except BadHeaderError:
                return HttpResponse('無効なヘッダが検出されました。')

            return redirect('index')

        # フォーム内容が妥当でなければ空のフォームを再表示
        return render(request, 'app/contact.html', {
            'form': form
    })