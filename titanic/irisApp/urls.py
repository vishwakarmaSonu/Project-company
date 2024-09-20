from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
    path('sonu/<slug:mata>',views.su,name='sonu'),
]