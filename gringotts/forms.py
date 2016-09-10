from django import forms

class NameForm(forms.Form):
    api_url = forms.CharField(label='api url', max_length=100)
    request_headers = forms.CharField(label='request headers', max_length=100)
    request_type = forms.CharField(label='request type', max_length=100)
    request_body = forms.CharField(label='request 	body', max_length=100,widget=forms.Textarea)
    response_headers = forms.CharField(label='response headers', max_length=100)
    response_body = forms.CharField(label='response body', max_length=100,widget=forms.Textarea)
