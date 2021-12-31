from django.conf.urls import url,include
from app.mascota.views import index_mascota,mascota_view,mascota_list,mascota_edit,mascota_delete,\
MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete

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
    
]




