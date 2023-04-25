from django import forms

FAVORITE_DISH = [
    ('Italian', 'Italian'),
    ('Greek', 'Greek'),
    ('Turkish', 'Turkish')
]
class DemoForm(forms.Form):
    name =  forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailField(label='Enter an email address')
    date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    choice = forms.ChoiceField(choices=FAVORITE_DISH) #select input field
    choice2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_DISH) #select input field