from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^home/',views.home, name='home'),
    url(r'^aboutBaMMmotif/', views.info, name='info'),
    url(r'^documentation/', views.documentation, name='documentation'),
    url(r'^download/', views.download, name='download'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^imprint/', views.imprint, name='imprint'),
    url(r'^job/$', views.data_predict, name='data_predict'),
    url(r'^job/data_predict/', views.data_predict, name='data_predict'),
    url(r'^job/data_discover/$', views.data_discover, name='data_discover'),
    url(r'^job/data_discover/(?P<pk>.*)/', views.data_discover_from_db, name='data_discover_from_db'),
    url(r'^job/submitted/', views.submitted, name='submitted'),
    url(r'^results/$', views.find_results, name='find_results'),
    url(r'^results/result_overview/$', views.result_overview, name='result_overview'),
    url(r'^results/(?P<pk>.*)/$', views.result_detail, name='result_detail'),
    url(r'^delete/(?P<pk>.*)/$', views.delete, name='delete'),
    url(r'^database/$', views.maindb, name='maindb'),
    url(r'^database/db_overview/$', views.db_overview, name='db_overview'),
    url(r'^database/(?P<pk>.*)/$', views.db_detail, name='db_detail'),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

