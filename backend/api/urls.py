from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('status/', views.status, name='status'),
    path('status/edit/<int:status_id>/', views.status_edit, name='status-edit'),
    path('status/delete/<int:pk>/', views.status_delete, name='status-delete'),
    path('status/mass-delete/', views.mass_delete_statuses, name='status-mass-delete'),
    path('status/delete_all/', views.delete_all_statuses, name='status-delete-all'),
    path('type/', views.type, name='type'),
    path('type/edit/<int:type_id>/', views.type_edit, name='type-edit'),
    path('type/delete/<int:pk>/', views.one_type_delete, name='type-delete'),
    path('type/mass-delete/', views.mass_delete_types, name='type-mass-delete'),
    path('type/delete_all/', views.delete_all_types, name='type-delete-all'),
]