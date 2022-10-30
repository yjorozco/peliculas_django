from django.conf import settings
from django.conf.urls import url
from director import views
urlpatterns = [
    url(r'^peliculas/$',views.index,name="index"),
] 