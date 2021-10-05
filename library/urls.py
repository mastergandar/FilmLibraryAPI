from django.urls import path
from rest_framework import routers

from library import views

app_name = 'Library api'

router = routers.SimpleRouter()

urlpatterns = [
    path('', views.LibraryListView.as_view(), name='list'),
    path('<int:pk>', views.LibraryRetrieveUpdateDestroy.as_view(), name='retrieve_update_destroy'),
    path('<int:pk>/product', views.LibraryProductsListView.as_view(), name='list'),
    path('<int:pk>/product/<int:content_pk>', views.LibraryProductsRetrieveUpdateDestroy.as_view(),
         name='create_retrieve_update_destroy'),
]

urlpatterns += router.urls
