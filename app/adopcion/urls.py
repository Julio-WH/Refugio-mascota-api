from django.conf.urls import url,include
from app.adopcion.views import index_adopcion,AdopcionList,AdopcionCreate,AdopcionUpdate,\
AdopcionDelete,SolicitudList,SolicitudCreate,SolicitudUpdate,SolicitudDelete

urlpatterns = [
    url(r'^index$', index_adopcion,name='index'),
    url(r'^lista$', AdopcionList.as_view(),name='adopcion_lista'),
    url(r'^nuevo$', AdopcionCreate.as_view(),name='adopcion_crear'),
    url(r'^editar/(?P<pk>\d+)/$', AdopcionUpdate.as_view(),name='adopcion_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', AdopcionDelete.as_view(),name='adopcion_eliminar'),
    url(r'^solicitud/lista$', SolicitudList.as_view(),name='solicitud_lista'),
    url(r'^solicitud/nuevo$', SolicitudCreate.as_view(),name='solicitud_nuevo'),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(),name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(),name='solicitud_eliminar'),


]