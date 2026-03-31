from django.contrib.auth import views as auth_views
from django.urls import path 
from . import views

urlpatterns = [

    #Autentificare

    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Home
    path('', views.home, name='home'),
    
    # URLs pentru Membri
    path('membri/', views.membru_list, name='membru_list'),
    path('membri/<int:pk>/', views.membru_detail, name='membru_detail'),
    path('membri/nou/', views.membru_create, name='membru_create'),
    path('membri/<int:pk>/modifica/', views.membru_update, name='membru_update'),
    path('membri/<int:pk>/sterge/', views.membru_delete, name='membru_delete'),
    
    # URLs pentru Trupe
    path('trupe/', views.trupa_list, name='trupa_list'),
    path('trupe/<int:pk>/', views.trupa_detail, name='trupa_detail'),
    path('trupe/nou/', views.trupa_create, name='trupa_create'),
    path('trupe/<int:pk>/modifica/', views.trupa_update, name='trupa_update'),
    path('trupe/<int:pk>/sterge/', views.trupa_delete, name='trupa_delete'),
    
    # URLs pentru MembruTrupa
    path('membru-trupa/', views.membrutrupa_list, name='membrutrupa_list'),
    path('membru-trupa/<int:pk>/', views.membrutrupa_detail, name='membrutrupa_detail'),
    path('membru-trupa/nou/', views.membrutrupa_create, name='membrutrupa_create'),
    path('membru-trupa/<int:pk>/modifica/', views.membrutrupa_update, name='membrutrupa_update'),
    path('membru-trupa/<int:pk>/sterge/', views.membrutrupa_delete, name='membrutrupa_delete'),
]