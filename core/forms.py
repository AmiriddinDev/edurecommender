from django import forms

# Baholar formasi
class GradeForm(forms.Form):
    matematika = forms.IntegerField(label="Matematika", min_value=0, max_value=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fizika = forms.IntegerField(label="Fizika", min_value=0, max_value=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    biologiya = forms.IntegerField(label="Biologiya", min_value=0, max_value=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    informatika = forms.IntegerField(label="Informatika", min_value=0, max_value=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    tarix = forms.IntegerField(label="Tarix", min_value=0, max_value=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ingliz_tili = forms.IntegerField(label="Ingliz tili", min_value=0, max_value=10, widget=forms.NumberInput(attrs={'class': 'form-control'}))
