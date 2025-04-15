import joblib
import os

from django.shortcuts import render
from .forms import SubjectForm

# Modelni yuklaymiz
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'recommender_model.pkl')
model = joblib.load(MODEL_PATH)

def home(request):
    result = None
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = [
                data['matematika'],
                data['fizika'],
                data['biologiya'],
                data['informatika'],
                data['tarix'],
                data['ingliz_tili']
            ]
            prediction = model.predict([input_data])[0]
            result = f"Siz uchun eng mos yo‘nalish: {prediction} ✅"
    else:
        form = SubjectForm()
    return render(request, 'core/form.html', {'form': form, 'result': result})
