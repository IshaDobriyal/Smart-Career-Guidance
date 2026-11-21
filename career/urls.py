from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('skill-analysis/', views.skill_analysis, name='skill_analysis'),
    
    path('roadmap/', views.career_roadmap, name='roadmap'),

]
