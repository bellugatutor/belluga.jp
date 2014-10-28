from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = i18n_patterns('',
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
)

urlpatterns += patterns('',
    url(r'^setlang/$', 'django.views.i18n.set_language', name='set_language'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
