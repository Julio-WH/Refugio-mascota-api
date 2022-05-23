from django.conf.urls import url,include
from app.mascota.views import index_mascota, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, api_list, api_edit, api_edit2, api_add, api_delete,\
    api_mascota_persona, api_edit3

urlpatterns = [
    url(r'^$', index_mascota,name='index'),
    url(r'^nuevo$', mascota_view,name='mascota_crear'),
    url(r'^lista$', mascota_list,name='mascota_lista'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit,name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete,name='mascota_eliminar'),
    url(r'^class/lista$', MascotaList.as_view(),name='mascota_class_lista'),
    url(r'^class/nuevo$', MascotaCreate.as_view(),name='mascota_class_nuevo'),
    url(r'^class/editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(),name='mascota_class_editar'),
    url(r'^class/eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(),name='mascota_class_eliminar'),
    #------api------#
    url(r'^lista-api/(?P<tipo_api>[\w\-]+)/$', api_list, name='api_list'),
    url(r'^(?P<tipo_api>[\w\-]+)/agregar/$', api_add, name='api_add'),
    url(r'^(?P<tipo_api>[\w\-]+)/editar/(?P<id_mascota>\d+)/$', api_edit, name='api_edit'),
    url(r'^(?P<tipo_api>[\w\-]+)/eliminar/(?P<id_mascota>\d+)/$', api_delete, name='api_delete'),
    url(r'^(?P<tipo_api>[\w\-]+)/(?P<id_mascota>\d+)/persona$', api_mascota_persona, name='api_mascota_persona'),
    url(r'^ApiView/editar2/(?P<id_mascota>\d+)/$', api_edit2, name='api_edit2'),
    url(r'^ApiView/editar3/(?P<id_mascota>\d+)/$', api_edit3, name='api_edit3'),

    
]




