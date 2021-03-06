from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.list_detail import object_list, object_detail

from django.views.generic.simple import redirect_to

from ncfmusic.apps.content.models import *

handler500 = 'ncfmusic.apps.content.views.server_error'

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/',    include('grappelli.urls')),
    (r'^admin/doc/',    include('django.contrib.admindocs.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/',        include(admin.site.urls)),
)

if True: #settings.DEBUG:
  urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    (r'500/$', 'ncfmusic.apps.content.views.server_error'),
  )

blog_dict = {
    'queryset': BlogEntry.objects.all(),
    'extra_context': {
        'content_page': Page.objects.get(slug='blog'),
        'categories': BlogCategory.objects.order_by('name'),
    },
}

urlpatterns += patterns('ncfmusic.apps.content.views',
    #(r'^admin/content/conferenceregistrations/csv/$','export_registrations'),
    (r'^about/$',                                   'about'),
    (r'^listen/$',                                  'listen'),
    (r'^podcast/$',                                 'podcast'),
    (r'^watch/$',                                   'watch'),
    (r'^watch/(?P<slug>[\w-]+)/$',                  'watch'),
    (r'^learn/$',                                   'learn'),
    (r'^learn/(?P<tag>[\w-]+)/$',                   'learn'),
    (r'^lessons/$',                                 'tutorials'),
    (r'^lessons/(?P<slug>[\w-]+)/$',                'tutorial'),
    (r'^talks/$',                                   'talks'),
    (r'^talks/(?P<slug>[\w-]+)/$',                  'talk'),
    (r'^articles/$',                                'articles'),
    (r'^articles/(?P<slug>[\w-]+)/$',               'article'),
    
    (r'^blog/$', redirect_to, {'url': '/updates/'}),
    (r'^blog/page/(?P<page>[0-9]+)/$', redirect_to, {'url': '/updates/page/%(page)s/'}),
    (r'^blog/category/(?P<slug>[\w-]+)/$', redirect_to, {'url': '/updates/category/%(slug)s/'}),
    (r'^blog/(?P<slug>[\w-]+)/$', redirect_to, {'url': '/updates/%(slug)s/'}),

    (r'^updates/$',                                 object_list, dict(blog_dict, paginate_by=7)),
    (r'^updates/page/(?P<page>[0-9]+)/$',           object_list, blog_dict),
    (r'^updates/category/(?P<slug>[\w-]+)/$',       'blog_category_list'),
    (r'^updates/(?P<slug>[\w-]+)/$',                   object_detail, dict(blog_dict, slug_field='slug')),
    #(r'^songs/$',                                   'songs'),
    #(r'^songs/(?P<start_letter>\w{1})/$',           'songs'),

    #('^foo/(?P<id>\d+)/$', redirect_to, {'url': '/bar/%(id)s/'}),



    (r'^events/$',                                  'events'),
    (r'^events/(?P<month>\d{2})/(?P<year>\d{4})/$', 'events'),
    (r'^events/(?P<slug>[\w-]+)/$',                 'event'),
    #(r'^contributors/$',                            'churches'),
    #(r'^churches/$',                                'churches'),
    #(r'^churches/(?P<slug>[\w-]+)/$',               'church'),
    #(r'^musicians/$',                               'musicians'),
    #(r'^musicians/(?P<slug>[\w-]+)/$',              'musicians'),
    (r'^search/$',                                  'search'),
    (r'^resources/$',                               'resources'),
    (r'^resources/type/(?P<resource_type>[\w-]+)/$','resources'),
    (r'^resources/type/(?P<resource_type>[\w-]+)/genre/(?P<genre>[\w-]+)/$', 'resources'),
    (r'^resources/genre/(?P<genre>[\w-]+)/$',       'resources'),
    (r'^resources/genre/(?P<genre>[\w-]+)/type/(?P<resource_type>[\w-]+)/$', 'resources'),
    (r'^resources/tag/(?P<tag>[\w-]+)/$',           'resources'),
    (r'^resources/tag/(?P<tag>[\w-]+)/genre/(?P<genre>[\w-]+)/$', 'resources'),
    (r'^resource/(?P<slug>[\w-]+)/$',               'resource'),
    #(r'^conference/$',                              'conference'),
    #(r'^conference/registration/$',                 'conference_registration'),
    #(r'^conference/registration/thanks/$',          'conference_registration_thanks'),
    (r'^paypal-return/$',                           'paypal_return'),
    (r'^facebook/$',                                'facebook_auth_post'),
    (r'^(?P<slug>[\w-]+)/$',                        'standalone_page'),

    (r'^$',                                         'home'),
)

