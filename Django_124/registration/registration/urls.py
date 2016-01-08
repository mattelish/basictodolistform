from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'registration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registrationform/', include('registrationform.urls', namespace="registrationform")),
    url(r'^admin/', include(admin.site.urls)),
]
