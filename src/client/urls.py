from django.urls import path
from client.endpoint import auth_views

urlpatterns = [
    path('teachbase-callback/', auth_views.teachbase_auth),
]