from django.conf.urls import url,include
from app.adopcion.views import index_adopcion,AdopcionList,AdopcionCreate,AdopcionUpdate,\
AdopcionDelete,SolicitudList,SolicitudCreate,SolicitudUpdate,SolicitudDelete,\
adopcion_list,adopcion_view,adopcion_edit,adopcion_delete

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
    url(r'^funct/lista$', adopcion_list,name='adopcion_funct_lista'),
    url(r'^funct/nuevo$', adopcion_view,name='adopcion_funct_crear'),
    url(r'^funct/editar/(?P<id_adopcion>\d+)/$', adopcion_edit,name='adopcion_funct_editar'),
    url(r'^funct/eliminar/(?P<id_adopcion>\d+)/$', adopcion_delete,name='adopcion_funct_eliminar'),

]