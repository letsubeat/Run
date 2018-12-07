from django.urls import path, re_path
from blog.views import *

urlpatterns = [
    path('', PostLV.as_view(), name='post-index'),
    path('post', PostLV.as_view(), name='post_list'),
    path('post/<slug>', PostDV.as_view(), name='post_detail'),
    path('archive', PostAV.as_view(), name='post_archive'),
    re_path(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>[0-9]{1,2})$', PostDAV.as_view(), name='post_day_archive'),
    path('today', PostTAV.as_view(), name='post_today_archive'),
    path('tag', TagTV.as_view(), name='tag-cloud'),
    path('tag/<str:tag>', PostTOL.as_view(), name='tagged-object-list'),
    path('search', SearchFormView.as_view(), name='search'),
]
