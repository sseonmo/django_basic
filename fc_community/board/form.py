from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(max_length=128, label='제목', error_messages={
        'required': '제목를 입력해주세요'})
    contents = forms.CharField(widget=forms.Textarea, label='내용', error_messages={
                               'required': '내용를 입력해주세요'})
    tags = forms.CharField(required=False, label='태그')
