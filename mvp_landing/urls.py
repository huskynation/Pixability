from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^our-story/$', 'signups.views.ourstory', name='ourstory'),
    url(r'^team/$', 'signups.views.team', name='team'),
    url(r'^blog/$', 'signups.views.blog', name='blog'),
    url(r'^borrower/$', 'signups.views.borrower', name='borrower'),
    url(r'^lender/$', 'signups.views.lender', name='lender'),
    url(r'^process/$', 'signups.views.process', name='process'),
    url(r'^careers/$', 'signups.views.careers', name='careers'),
    url(r'^upload/$', 'signups.views.upload', name='upload'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)