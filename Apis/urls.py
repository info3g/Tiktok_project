
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='home'),
    path('info', views.UserInfoList.as_view()),
    path('Video/', views.UserVideo.as_view()),
    path('homes/',views.homes,name='homes'),
    path('test/',views.test,name='test')
]



# http://172.104.154.156:3000/v1/insertDeepScouting?id=d0dd6e0cf620541fdd14527cc9a9813a&signature=IPKIdHHQQ8ahWxzLro4OhPNXV48=&followers=764&following=655&profile_photo=https://instagram.fixc2-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/244376991_1237263960110436_5985419241198437524_n.jpg?nc_ht=instagram.fixc2-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=2-U2p-IrMYAX-YG8V4&edm=AAuNW_gBAAAA&ccb=7-4&oh=acab62cd4814e5954cfa4fc459561c3e&oe=6178D207&_nc_sid=498da5&blocked=description=photos[%27https://instagram.fixc1-4.fna.fbcdn.net/v/t51.2885-19/s320x320/235175318_1780462225460153_8809187701344432145_n.jpg?_nc_ht=instagram.fixc1-4.fna.fbcdn.net&_nc_ohc=RukLQhiiQ6kAX962vmG&edm=AAuNW_gBAAAA&ccb=7-4&oh=627ea095da1ba2ac9b4434952117a029&oe=6176DB45&_nc_sid=498da5%27]=&trace_id=617685c1421aa95d4e52ddeb&instagram=jackiefontijn_


# http://172.104.154.156:3000/v1/insertDeepScouting?id=d0dd6e0cf620541fdd14527cc9a9813a&signature=IPKIdHHQQ8ahWxzLro4OhPNXV48=&followers=764&following=655&profile_photo
# =https://instagram.fixc2-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/244376991_1237263960110436_5985419241198437524_n.jpg?nc_ht=instagram.fixc2-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=2-U2p-IrMYAX-YG8V4&edm=AAuNW_gBAAAA&ccb=7-4&oh=acab62cd4814e5954cfa4fc459561c3e&oe=6178D207&_nc_sid=498da5&blocked=description=
# photos[%27https://instagram.fixc1-4.fna.fbcdn.net/v/t51.2885-19/s320x320/235175318_1780462225460153_8809187701344432145_n.jpg?_nc_ht=instagram.fixc1-4.fna.fbcdn.net&_nc_ohc=RukLQhiiQ6kAX962vmG&edm=AAuNW_gBAAAA&ccb=7-4&oh=627ea095da1ba2ac9b4434952117a029&oe=6176DB45&_nc_sid=498da5%27]=&trace_id=61753598421aa91bc9d3cf49&instagram=testuser


# http://172.104.154.156:3000/v1/insertDeepScouting?id=d0dd6e0cf620541fdd14527cc9a9813a&signature=d0dd6e0cf620541fdd14527cc9a9813a-61753598421aa91bc9d3cf49-testing-02a21adad3229c35f5bfc20ecbbb9ae1&followers=764&following=655&profile_photo=https://instagram.fixc2-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/244376991_1237263960110436_5985419241198437524_n.jpg?nc_ht=instagram.fixc2-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=2-U2p-IrMYAX-YG8V4&edm=AAuNW_gBAAAA&ccb=7-4&oh=acab62cd4814e5954cfa4fc459561c3e&oe=6178D207&_nc_sid=498da5&blocked=0&description=1&photos=[%27https://instagram.fixc1-4.fna.fbcdn.net/v/t51.2885-19/s320x320/235175318_1780462225460153_8809187701344432145_n.jpg?_nc_ht=instagram.fixc1-4.fna.fbcdn.net&_nc_ohc=RukLQhiiQ6kAX962vmG&edm=AAuNW_gBAAAA&ccb=7-4&oh=627ea095da1ba2ac9b4434952117a029&oe=6176DB45&_nc_sid=498da5%27]=&trace_id=61753598421aa91bc9d3cf49&instagram=testing