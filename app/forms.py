from django import forms

class ContactForm(forms.Form):
    """
    問い合わせページ用
    """
    name = forms.CharField(max_length=100, label='名前')
    email = forms.EmailField(max_length=100, label='あなたのメールアドレス')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea())