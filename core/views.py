from django.shortcuts import render
import joblib
import os

from core.forms import GradeForm

# Modelni yuklab olish
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'recommender_model.pkl')
model = joblib.load(MODEL_PATH)


# Home view: forma va natija ko‘rsatish
def home(request):
    return render(request, template_name="index.html")

def render_form(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            data = list(form.cleaned_data.values())
            recommendation = model.predict([data])[0]
            return render(request, 'core/result.html', {
                'recommendation': recommendation
            })
    else:
        form = GradeForm()

    return render(request, 'core/form.html', {
        'form': form
    })
