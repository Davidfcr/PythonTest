"""
PythonTest URL Configuration
"""
from django.conf.urls import url
from django.conf.urls import patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^crudmenu/$', TemplateView.as_view(template_name='crudmenu.html'), name='crudmenu'),
    url(r'^crudmenu/(?P<table>[\w|\W]+)/$', 'Main.views.crudselect_view', name='crudselect'),
    url(r'^crudarticlecreate/$', 'Article.views.article_create', name='crudarticlecreate'),
    url(r'^crudarticleupdate/(?P<pk>\d+)/$', 'Article.views.article_update', name='crudarticleupdate'),
    url(r'^crudarticledelete/(?P<pk>\d+)/$', 'Article.views.article_delete', name='crudarticledelete'),
    url(r'^crudstorecreate/$', 'Store.views.store_create', name='crudstorecreate'),
    url(r'^crudstoreupdate/(?P<pk>\d+)/$', 'Store.views.store_update', name='crudstoreupdate'),
    url(r'^crudstoredelete/(?P<pk>\d+)/$', 'Store.views.store_delete', name='crudstoredelete'),
    url(r'^services/$', TemplateView.as_view(template_name='APIservices.html'), name='apiservices'),
    # API Rest JSON
    url(r'^services/article/$', 'Article.views.article_collection', name='article_collection'),
    url(r'^services/store/$', 'Store.views.store_collection', name='store_collection'),
    url(r'^services/article/(?P<key>\d+)/$', 'Article.views.article_by_store_element', name='articlebystore_collection'),
    # API Rest XML
    url(r'^services/articlexml/$', 'Article.views.article_collection_xml', name='article_collection_xml'),
    url(r'^services/storexml/$', 'Store.views.store_collection_xml', name='store_collection_xml'),
    url(r'^services/articlexml/(?P<key>\d+)/$', 'Article.views.article_by_store_element_xml', name='articlebystore_collection_xml'),
    #url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
