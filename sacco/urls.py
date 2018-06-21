from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
     name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
     name='password_change_done'),
    url(r'^reset/$',
     auth_views.PasswordResetView.as_view(
      template_name='password_reset.html',
      email_template_name='password_reset_email.html',
      subject_template_name='password_reset_subject.txt'),
      name='password_reset'),
    url(r'^reset/done/$',
     auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
      name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
      name='password_reset_confirm'),
    url(r'^reset/complete/$',
     auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
      name='password_reset_complete'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
    url(r'^accounts/(?P<username>[\w.@+-]+)/$',views.accountCreation,name='accountCreation'),
    url(r'^loans/(?P<username>[\w.@+-]+)/$',views.loanApplication,name='loanApplication'),
    url(r'^loans/(?P<username>[\w.@+-]+)/(?P<loanNumber>\d+)/$',views.loanPayment,name='loanPayment'),
    url(r'^accounts/(?P<username>[\w.@+-]+)/(?P<accountNumber>\d+)/$',views.accountDeposit,name='accountDeposit'),
    url(r'^register$',views.register , name="register"),
    url(r'^contact$',views.contact , name="contact"),
    url(r'^$',views.index , name="index"),



]
