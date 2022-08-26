

from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name = 'articleApp'
urlpatterns = [
    path('',views.articleview,name='articleList'),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('article/',views.addarticle,name='article'),
    path('draft/',views.draftview,name='draft'),
    path('delete/<int:id>',views.delete_article,name='delete'),
    path('update/<int:id>',views.update_article,name='update'),
    path('articleList/',views.articleview,name='articleList'),
    path('myarticle/',views.my_article,name='myarticle'),  

]
