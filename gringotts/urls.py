from django.conf.urls import include, url
from django.contrib import admin
from gringotts.api import APIResource

api_resource = APIResource()

urlpatterns = [
    # Examples:
    # url(r'^$', 'gringotts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'gringotts.views.home', name='home'),
    url(r'^get_data/', 'gringotts.views.get_data', name='get_data'),
    url(r'^api/', include(api_resource.urls)),
]
