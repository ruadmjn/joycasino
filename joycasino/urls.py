from django.conf.urls import url
from joycasino import views

urlpatterns = [
    url(r'^$', views.index),
]
