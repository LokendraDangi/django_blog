from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('post/create/', views.createpost, name="createpost"),
    path('post/list/', views.listpost, name="listpost"),
    path('post/<int:id>/edit/', views.editpost, name="editpost"),
    path('post/<int:id>/delete/', views.deletepost, name="deletepost"),
    path('post/<str:slug>', views.postdetail, name="postdetail"),
    path('category/<str:slug>', views.categorydetail, name="categorydetail"),
]