from django.urls import path

from core.views import home, render_form

app_name = 'core'

urlpatterns = [
    path('', home, name='index'),
    path('render-form/', render_form, name='render_form'),
]