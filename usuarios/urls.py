from django.urls import path
from .views import cadastro, login_, logout_

urlpatterns = [
    path("login/", login_, name="login"),
    path("cadastro/", cadastro, name="cadastro"),
    path("logout/", logout_, name="logout"),
]
