from ieee import views
from django.conf.urls import url
urlpatterns=[
    url('home-page',views.HomePage),
    url('register-page/',views.RegisterPage),
    url('instruction-page/',views.InstructionPage),
    url('candidate-page/',views.CandidatePage),
    url('add/',views.Add),
    url('edit-page/',views.EditPage),
    url('edit/',views.Edit),
    url('delete-page/',views.DeletePage),
    url('login-page/',views.LoginPage),
    url('logout-page/',views.LogoutPage),
    url('signup-page/',views.SignupPage),
]
