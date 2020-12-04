from django.urls import path
from pojedine import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('struja/', views.StrujaView.as_view(), name='struja'),
    path('plin/', views.PlinView.as_view(), name='plin'),
    path('voda/', views.VodaView.as_view(), name='voda'),
]
