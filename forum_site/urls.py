"""forum_site URL Configuration
    
    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/1.11/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.conf.urls import url, include
        2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    """


from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from forum import views
from forum.views import get_article,get_index,get_posts,post_post,post_article,put_article,delete_article,delete_comment
from forum.views import index_login,index_register

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^index/$',get_index,name="index"),
        url(r'^plate/(?P<id>\d+)/$',get_posts,name='plate'),
        # url(r'^plate/(?P<id>\d+)/$',views.articleBack,name='plate'),
        url(r'^plate/(?P<id>\d+)/post/$',post_post),
        url(r'^article/(?P<id>\d+)/$',get_article,name='article'),
        url(r'^article/(?P<id>\d+)/comment/$',post_article),
        url(r'^article/(?P<id>\d+)/comment/delete/$',delete_comment),
        url(r'^article/(?P<id>\d+)/put/$',put_article),
        url(r'^article/(?P<id>\d+)/delete/$',delete_article),
        url(r'^login/', index_login, name="login"),
        url(r'^register/', index_register, name="register"),
        path('addFriend/',views.addFriend),
        path('userpage/',views.userpage),
        path('infoset/',views.infoset),
        path('comment/',views.comment),
        path('repost/',views.repost),
    ]

