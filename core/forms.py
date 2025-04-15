from django import forms

class SubjectForm(forms.Form):
    matematika = forms.IntegerField(label='Matematika', min_value=0, max_value=10)
    fizika = forms.IntegerField(label='Fizika', min_value=0, max_value=10)
    biologiya = forms.IntegerField(label='Biologiya', min_value=0, max_value=10)
    informatika = forms.IntegerField(label='Informatika', min_value=0, max_value=10)
    tarix = forms.IntegerField(label='Tarix', min_value=0, max_value=10)
    ingliz_tili = forms.IntegerField(label='Ingliz tili', min_value=0, max_value=10)
