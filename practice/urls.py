from .import views
from django.urls import path
# from .views import index, detail, update, delete

urlpatterns = [
    path('', views.index, name='index-shoppin'),
    path('details/', views.detail, name='details'),
    path('collection/', views.collection, name='collection'),
    # collection/id/                detail page with id
    path('collection/<int:id>/', views.collection_detail, name='collection'),
    #collection/id/delete
    path('collection/<int:pk>/delete/', views.Delete.as_view(), name='delete'),
    path('update/<int:id>/', views.Update, name='update'),
    path('create/', views.Create, name='create'),
    path('per/', views.per, name='per'),
    # path('delete/<init:id>/', views.human_delete_view, name='delete'),

]