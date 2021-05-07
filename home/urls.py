from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('api', views.api.as_view(), name='api'),
]
