from django import forms
from .models import EggInfo
from .choices import *
from django.forms import ModelForm
class AddEggForm(forms.Form):
          breed= forms.CharField(
              max_length=100,
              label="Specify breed of egg:",
              #widget=forms.TextInput(attrs={'required': "required"})
          )

          eggType = forms.ChoiceField(
              choices=EGG_TYPE,
              label="Select Type of Egg:",
              initial='',
              widget=forms.Select(),
              required=True
          )

          eggSize = forms.ChoiceField(
              choices=EGG_SIZE,
              label="Select Size of Egg",
              initial='',
              widget=forms.Select(),
              required=True
          )


class DeleteEggForm(forms.Form):
    eggToDelete = forms.ModelChoiceField(queryset=EggInfo.objects.all())

class ClearAllEggsFromDBForm(forms.Form):
    field = forms.TypedChoiceField(label = "Select an option:",coerce=lambda x: x == 'True',
                                   choices=((False, 'No'), (True, 'Yes')))
def clean(self):
    cleaned_data = super(AddEggForm, self).clean()
    breed = cleaned_data.get('breed')
    eggType = cleaned_data.get('eggType')
    eggSize = cleaned_data.get('eggSize')
    if not breed and not eggType and not eggSize:
        raise forms.ValidationError('You have to write something!')

class TemperatureForm(forms.Form):
    temperatureChoice = forms.ChoiceField(
        choices=TEMPERATURE,
        label="Select Temperature you wish to output for your readings:",
        initial='',
        widget=forms.Select(),
        required=True
    )
class TimeUnitForm(forms.Form):
    TimeChoice = forms.ChoiceField(
        choices=TIME_UNITS,
        label="Select Time Units you wish to use:",
        initial='',
        widget=forms.Select(),
        required=True
    )
class TimerForm(forms.Form):
    DaysInTimer = forms.ChoiceField(
        choices=DAYS,
        label="Select Number of Days:",
        initial='',
        widget=forms.Select(),
        required=True
    )
    HoursInTimer = forms.ChoiceField(
        choices=HOURS,
        label="Select Number of Hours:",
        initial='',
        widget=forms.Select(),
        required=True
    )
    MinutesInTimer = forms.ChoiceField(
        choices=MINUTES,
        label="Select Number of Minutes:",
        initial='',
        widget=forms.Select(),
        required=True
    )
    SecondsInTimer=InTimer = forms.ChoiceField(
        choices=SECONDS,
        label="Select Number of Seconds",
        initial='',
        widget=forms.Select(),
        required=True
    )
