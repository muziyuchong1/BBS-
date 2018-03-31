from boards import views
from django.conf.urls import url
from django.contrib import admin
from accounts import views as accounts_views #使用as ,别名是为了避免与boards的视图产生冲突
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^signup/$',accounts_views.signup,name='signup'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^boards/(?P<pk>\d+)/$',views.board_topics,name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$',views.new_topic,name = 'new_topic'),
    url(r'^admin/', admin.site.urls),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name = 'password_reset.html',
            email_template_name = 'password_reset_email.html',
            subject_template_name = 'password_reset_subject.txt'
        ),
        name = 'password_reset'),

    url(r'reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name = 'password_reset_done.html'),
            name = 'password_reset_done'
        ),

    url(r'reset/(?P<uidb64>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'),
        name = 'password_reset_confirm'),

    url(r'reset/complete/$',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name = 'password_reset_complete'),


    #密码更改视图(更改密码的登陆用户使用,这些表单有三个字段组成:旧密码,新密码,新密码确认)
    #这些视图仅适用于登录用户。他们使用一个名为的视图装饰器@login_required。此装饰器可防止非授权用户访问此页面。如果用户没有登录，Django会将他们重定向到登录页面

    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),


    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),

#url处理两个关键字参数,pk用于标识bo
    # ard,现在我们已经用topic_pk它来确定从数据库中检索哪个主题。

]
