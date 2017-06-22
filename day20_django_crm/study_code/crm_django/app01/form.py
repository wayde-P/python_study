from django import forms
from app01 import models
import re

favorite_colors_choices = (
    ('blue', 'BLUE'),
    ('red', 'RED'),
    ('black', 'BLACK'),
)

BIRTH_YEAR_CHOICES = ('1980', '1982', '1984', '1986', '1989',)


class MailSendForm(forms.Form):
    sender = forms.EmailField()
    receiver = forms.EmailField()
    subject = forms.CharField(max_length=15)
    content = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 100,
        'class': 'font=color',
        'sytle': 'background-color:lightgreen'
    }))
    birth_day = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    seat_CHOICES = (('1', 'First'), ('2', 'Second'),)

    def mobile_validate(value):
        mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
        if not mobile_re.match(str(value)):
            raise forms.ValidationError('手机号码格式错误')

    mobile = forms.IntegerField(validators=[mobile_validate, ],
                                error_messages={'required': "手机不能为空"},
                                widget=forms.TextInput(attrs={'class': "form-control",
                                                              'placeholder': "手机号码"})
                                )

    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=seat_CHOICES)
    favorite_colors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=favorite_colors_choices,
    )

    def clean_sender(self):
        print("validate sender", self.cleaned_data)
        if self.cleaned_data.get("sender") != "alex@126.com":
            self.add_error("sender", "only alex has right to send mail")

        return self.cleaned_data.get("sender")

    def clean(self):
        print("clean data:::", self.cleaned_data)

        sender = self.cleaned_data.get('sender')
        receiver = self.cleaned_data.get('receiver')

        if sender == receiver:
            raise forms.ValidationError("发送和接受者不能相同")


class Bookmgr(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
        # fields = ['columea','columeb']
        # exclude = ['colume']
