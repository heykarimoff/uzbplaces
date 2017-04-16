from django.conf.urls import url

from apps.address import views

urlpatterns = [
    url(r'^provinces/$', views.ProvinceList.as_view(), name='provinces'),
    url(r'^regions/(?P<province>[0-9]+)/$', views.RegionList.as_view(), name='province_regions'),
    url(r'^regions/(?P<province>[0-9]+)/(?P<code>[0-9]+)/$', views.RegionDetail.as_view(), name='region_detail'),

]
