from django.conf.urls import patterns, include, url

from mainsploosh import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'mainsploosh.views.index', name='index'),

    # Examples:
    # url(r'^$', 'pennsploosh.views.home', name='home'),
    # url(r'^pennsploosh/', include('pennsploosh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
