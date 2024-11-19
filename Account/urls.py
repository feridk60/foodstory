from django.urls import path

from Account.views import  login_view, logout_view, register_view
# from django.contrib.auth.views import  PasswordResetCompleteView


urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view,name='register'),
    
    # 
    # path('change_password/',ChangePasswordView.as_view(),name='change_password'),

    # path('reset_password/', ResetPasswordView.as_view(), name = 'reset_password'),
    # path('reset_password_confirm/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    # path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),name='reset_password_complete'),

]



