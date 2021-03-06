from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import os.path
admin.autodiscover()

site_media_root = os.path.join(os.path.dirname(__file__),"media")

redirect_after_logout = getattr(settings, 'LOGOUT_REDIRECT_URL', None)
auth_urls = (r'^accounts/',include('django.contrib.auth.urls'))
logout_page = (r'^accounts/logout/$','django.contrib.auth.views.logout', {'next_page': redirect_after_logout})
if hasattr(settings,'WIND_BASE'):
    auth_urls = (r'^accounts/',include('djangowind.urls'))
    logout_page = (r'^accounts/logout/$','djangowind.views.logout', {'next_page': redirect_after_logout})

urlpatterns = patterns('',
                       # Example:
                       # (r'^faktum/', include('faktum.foo.urls')),
		       auth_urls,
		       logout_page,
                       (r'^$','faktum.main.views.index'),
                       (r'^add/$','faktum.main.views.add'),
                       (r'^multiadd/$','faktum.main.views.multiadd'),
                       (r'^search/$','faktum.main.views.search'),
                       (r'^tag/(?P<tag_id>\d+)/$','faktum.main.views.tag'),
                       (r'^tag/$','faktum.main.views.tags'),
                       (r'^user/(?P<username>\w+)/$','faktum.main.views.user'),
                       (r'^fact/(?P<fact_id>\d+)/$','faktum.main.views.fact'),
                       (r'^registration/', include('registration.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
                       (r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) 

