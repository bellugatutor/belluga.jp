from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'accounts.views.home', name='home'),
    url(r'^signup/$', 'accounts.views.signup', name='signup'),
    url(r'^signup/tutor/$', 'accounts.views.signup_tutor', name='signup_tutor'),
    url(r'^login/$', 'accounts.views.login', name='login'),
    url(r'^logout/$', 'accounts.views.logout', name='logout'),
    url(r'^search/tutor/$', 'accounts.views.search_tutor', name='search_tutor'),
    url(r'^tutor/(\d+)/$', 'accounts.views.tutor_detail', name='tutor_detail'),
    url(r'^faq/$', 'accounts.views.faq', name='faq'),

    url(r'^howitwork/students/$', TemplateView.as_view(template_name='howitwork/students.html'), name='howitwork_students'),
    url(r'^howitwork/tutors/$', TemplateView.as_view(template_name='howitwork/tutors.html'), name='howitwork_tutors'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
