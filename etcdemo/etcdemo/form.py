from django import forms


class Demo01Form(forms.Form):

    textplus = forms.CharField(
        label='足す言葉',
        widget=forms.TextInput(
            attrs={
                'id': 'textplus',
                'placeholder': '単語を入力。複数の場合は空白で区切る。',
            }))

    textminus = forms.CharField(
        label='引く言葉',
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'textminus',
                'placeholder': '入力した単語を引き算します。',
            }))


class Demo02Form(forms.Form):

    areaone = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'id': 'resultbase64',
                "rows": 20,
                "cols": 10,
            }
        )
    )
