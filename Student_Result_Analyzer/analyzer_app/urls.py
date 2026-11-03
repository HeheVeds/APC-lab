from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('download/transcript/<str:roll_no>/', views.download_transcript, name='download_transcript'),
    path('download/class-summary/', views.download_class_summary, name='download_class_summary'),
    path('download/csv/', views.download_csv, name='download_csv'),
]
