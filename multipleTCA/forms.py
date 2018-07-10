from django import forms
import datetime as dt
from django.core import validators
from django.core.exceptions import ValidationError

class MinLengthValidator(validators.MinLengthValidator):
    message = 'Ensure this value has at least %(limit_value)d elements (it has %(show_value)d).'

class MaxLengthValidator(validators.MaxLengthValidator):
    message = 'Ensure this value has at most %(limit_value)d elements (it has %(show_value)d).'


class CommaSeparatedCharField(forms.Field):
    def __init__(self, dedup=True, max_length=None, min_length=None, *args, **kwargs):
        self.dedup, self.max_length, self.min_length = dedup, max_length, min_length
        super(CommaSeparatedCharField, self).__init__(*args, **kwargs)
        if min_length is not None:
            self.validators.append(MinLengthValidator(min_length))
        if max_length is not None:
            self.validators.append(MaxLengthValidator(max_length))

    def to_python(self, value):
        if value in validators.EMPTY_VALUES:
            return []

        value = [item.strip() for item in value.split(',') if item.strip()]
        if self.dedup:
            value = list(set(value))

        return value

    def clean(self, value):
        value = self.to_python(value)
        self.validate(value)
        self.run_validators(value)
        return value

class acc_date_Form(forms.Form):
    start_date  = forms.DateField(label = 'From', initial = dt.datetime.today()- dt.timedelta(days=7), widget=forms.DateInput(attrs={'type': 'date', 'class':"form-control", "style":"width: 163px; height: 41px; outline: none; margin-left:0px"}))
    end_date    = forms.DateField(label = 'To', initial = dt.datetime.today(), widget=forms.DateInput(attrs={'type': 'date', 'class':"form-control", "style":"width: 163px; height: 41px; outline: none; margin-left:0px"}))
    account_id  = CommaSeparatedCharField(label = "", max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols':40, 'class':"form-control", 'placeholder':" Account IDs"}))

    def clean(self):
        cleaned_data = super(acc_date_Form, self).clean()
        sd = cleaned_data.get('start_date')
        ed = cleaned_data.get('end_date')
        print (sd)
        print (ed)
        if(sd>ed):
            print ("ye ye ")
            # self.add_error('start_date', msg)
            raise forms.ValidationError("Start date > End Date")