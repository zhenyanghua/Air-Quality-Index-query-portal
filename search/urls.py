# aqi/search/urls.py
# Import django modules
from django.conf.urls import patterns, url


urlpatterns = patterns('search.views',
    url(r'^$', 'search_form', name='index'),
    url(r'^search-form/$','search_form', name='search-form'),
    url(r'^search/st/$','search_station',name='search-results'),
    url(r'^search/aqi/$','search_aqi',name='search-aqi'),
    url(r'^search/aqis/$','search_aqis',name='search-aqis'),
    #url(r'^search/aqi-export/$','exp2csv',name='exp2csv'),
)