from django.conf.urls import patterns, include, url
from interface.views import search

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Bangla_WordNet_online.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','interface.views.index',name='index'),
    url(r'^search/(\D+)/$','interface.views.search',name='search'),
    url(r'^about/$','interface.views.about',name='about'),
    url(r'^usage/$','interface.views.usage',name='usage')
)
