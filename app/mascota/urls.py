from django.conf.urls import url,include
from app.mascota.views import index_mascota,mascota_view,mascota_list,mascota_edit,mascota_delete

urlpatterns = [
    url(r'^$', index_mascota,name='index'),
    url(r'^nuevo$', mascota_view,name='mascota_crear'),
    url(r'^lista$', mascota_list,name='mascota_lista'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit,name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete,name='mascota_eliminar'),
    
]