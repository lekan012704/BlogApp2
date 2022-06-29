from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', IndexPage, name="Index" ),
    path('blog/category/<str:slug>', BlogHome, name="Blog" ),
    #path('blog/search', PostSearch, name="Search" ),
    path('blog/<str:slug>', PostDetail, name="details" ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
