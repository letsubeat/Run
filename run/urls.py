from django.contrib import admin
from django.urls import path, include

from run.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls, name='site-admin'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),

    # Class-based views for Bookmark app
    # path('bookmark/', BookMarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>/', BookMarkDV.as_view(), name='detail')
]
