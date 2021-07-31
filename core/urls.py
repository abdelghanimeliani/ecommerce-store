
from django.contrib import admin
from django.urls import path , include
from django.conf import settings 
from django.conf.urls.static import static


# including the store.urls to get accet to the store's urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls'), name='store'), 
]

# enfin hakda w mazal mafhamthach mlih
# Fonction utilitaire qui renvoie un motif d’URL pour servir les fichiers en mode débogage :

if settings.DEBUG : 
    urlpatterns+= static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)