from django import forms;

class InvestmentsValidator(forms.Form):
    user_id = forms.ModelChoiceField();
    capital = forms.DecimalField();
    assets_id = forms.ModelChoiceField();
    date_time = forms.CharField();
    is_buying = forms.BooleanField();
    amount = forms.IntegerField();