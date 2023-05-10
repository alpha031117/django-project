from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [    
    path('signin/', views.UserSignIn.as_view(), name="login-page"),
    path('signup/', views.UserSignUp.as_view(), name="signup-page"),
    path('logout/', views.UserLogOut.as_view(), name="logout-page"),
]