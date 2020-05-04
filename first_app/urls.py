from django.urls import path
from .views import UserList
from . import views

app_name = "first_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage/', views.form_name_view, name="form_name"),
    path('users/', views.users, name='users'),
    path('adduser/', views.add_user_view, name="add_user"),
    # path('usersjson/', views.userJson, name="user_json")
    path('login/', views.login, name="login"),
    path('current_user/', views.current_user),
    path('users_auth', UserList.as_view())
]


