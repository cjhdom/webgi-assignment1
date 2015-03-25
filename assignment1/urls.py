from django.conf.urls import patterns, include, url
from django.contrib import admin
from vote.views import *
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assignment1.views.home', name='home'),
	url(r'^vote/$',vote_view),
	url(r'^result/$',result_view),
    # url(r'^assignment1/', include('assignment1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
