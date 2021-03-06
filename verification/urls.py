from django.conf.urls import url
from verification import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    url('login/', views.login, name="login"),
    url('register/', views.register, name="register"),
    url('update_details/', views.UpdateDetails, name="updatedetails"),
    url('logout/', views.Logout, name="logout"),
    url(r'^password-reset/$', PasswordResetView.as_view(template_name="verification/password_reset.html"),
        name="password_reset"),
    url(r'^password-reset-done/$', PasswordResetDoneView.as_view(template_name="verification/password_reset_done.html"),
        name="password_reset_done"),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(template_name="verification/password_reset_confirm.html"),
        name="password_reset_confirm"),
    url(r'^password-reset-complete/$',
        PasswordResetCompleteView.as_view(template_name="verification/password_reset_complete.html"),
        name="password_reset_complete")
]
