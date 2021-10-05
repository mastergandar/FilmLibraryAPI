from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from films import views
from main import settings

app_name = 'Library api'

router = routers.SimpleRouter()

urlpatterns = [
    path('', views.FilmListCreateView.as_view(), name='list_create'),
    path('<int:pk>', views.FilmRetrieveUpdateDestroy.as_view(), name='retrieve_update_destroy'),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
