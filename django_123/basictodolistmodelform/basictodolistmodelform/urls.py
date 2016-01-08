from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', 'basictodolistmodelform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^todolist/', include('todolist.urls', namespace="todolist")),
    url(r'^admin/', include(admin.site.urls)),
]
