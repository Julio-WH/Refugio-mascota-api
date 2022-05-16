from django.conf.urls import url, include
from app.API.view.view_decorador import list_mascotas, detail_mascota, mascota_persona_list
from app.API.view.view_apiview import ListMascotas, DetalleMascota, MascotaPersonaList
from app.API.view.view_generic import MascotaListGeneric, MascotaDetailsGeneric, MascotaPersonaListGeneric
from app.API.view.view_set import MascotaViewset

urlpatterns = [
    #decoradores#
    url(r'^decorador/$', list_mascotas, name='decorador_mascota'),
    url(r'^decorador/detalle/(?P<pk>\d+)/$', detail_mascota, name='mascota_decorador_detalle'),
    url(r'^decorador/mascotas/(?P<pk>\d+)/persona/$', mascota_persona_list, name='mascota_persona_list_decorador'),
    #apiview#
    url(r'^apiview/$', ListMascotas.as_view(), name='apiview_mascota'),
    url(r'^apiview/detalle/(?P<pk>\d+)/$', DetalleMascota.as_view(), name='mascota_apiview_detalle'),
    url(r'^apiview/mascotas/(?P<pk>\d+)/persona/$', MascotaPersonaList.as_view(), name='mascota_persona_apiview_detalle'),
    #generic#
    url(r'^generic/$', MascotaListGeneric.as_view(), name='generic_mascota'),
    url(r'^generic/detalle/(?P<pk>\d+)/$', MascotaDetailsGeneric.as_view(), name='mascota_apiview_detalle'),
    url(r'^generic/mascotas/(?P<pk>\d+)/persona/$', MascotaPersonaListGeneric.as_view(), name='mascota_persona_generic'),
    #set#
    url(r'^set/$', MascotaViewset.as_view({'get': 'list', 'post': 'create'}), name='set_mascota'),
    url(r'^set/detalle/(?P<pk>\d+)/$', MascotaViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='set_detalle_mascota'),
    url(r'^set/mascotas/(?P<pk>\d+)/persona/', MascotaViewset.as_view({'get': 'persona'}), name='set_mascota_persona'),
]