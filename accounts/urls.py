from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('settings/change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html',success_url='/settings/change_password_done/'), name='change_password' ),
    path('settings/change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='change_password_done'),  # غير الاسم ليطابق ما يتوقعه Django
]
