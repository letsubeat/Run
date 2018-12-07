from django.urls import path

from bookmark.views import *

urlpatterns = [
    # Class-based views for Bookmark app
    path('', BookMarkLV.as_view(), name='bookmark-index'),
    path('<int:pk>', BookMarkDV.as_view(), name='bookmark-detail')
]
