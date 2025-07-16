from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LogoutView

from .views import profile_view, delete_account

urlpatterns = [
    path('add/', views.create_design, name='create_design'),
    path('', views.design_list, name='design_list'),
    path('register/', views.register, name='register'),
    path('design/<int:pk>/', views.design_detail, name='design_detail'),
    path('designer/<str:username>/', views.designer_profile, name='designer_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='designs/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('designs/<int:pk>/edit/', views.edit_design, name='edit_design'),
    path('password/', auth_views.PasswordChangeView.as_view(
    template_name='designs/password_change.html',
    success_url='/profile/'), name='password_change'),
    path('profile/', profile_view, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
]
