from django import forms

from .models import Member, Partner

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'