from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/$', 'blog.views.show_blog_entries'),
    url(r'^blog/info/$', 'blog.views.show_blog_info'),

    url(r'^blog/(?P<blog_id>\d+)/comment/$', 'blog.views.blog_comment'),

    url(r'^admin/', include(admin.site.urls)),
]
