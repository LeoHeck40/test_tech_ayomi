from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.connect, name='connect'),
    path('create_account', views.create, name='create'),
    path('connexion', views.connexion, name ='connexion'),
    path('logout',views.logout_view, name = 'logout'),
    path('creation', views.creation, name='creation'),
    path('modification/<str:user>', views.modif, name= 'modif'),
    path('enregistrer/<str:user>', views.enreg, name = 'enregistrer')
]