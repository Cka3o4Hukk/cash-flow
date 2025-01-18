from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),

    path('status/', include([
        path('', views.status, name='status'),
        path('edit/<int:status_id>/', views.status_edit, name='status_edit'),
        path('delete/<int:pk>/', views.status_delete, name='status_delete'),
        path('mass-delete/',
             views.mass_delete_statuses, name='status_mass_delete'),
        path('delete_all/',
             views.delete_all_statuses, name='status_delete_all'),
    ])),

    path('type/', include([
        path('', views.type, name='type'),
        path('edit/<int:type_id>/', views.type_edit, name='type_edit'),
        path('delete/<int:pk>/', views.one_type_delete, name='type_delete'),
        path('mass-delete/', views.mass_delete_types, name='type_mass_delete'),
        path('delete_all/', views.delete_all_types, name='type_delete_all'),
    ])),

    path('categories/', include([
        path('',
             views.category_list, name='category_list'),
        path('edit/<int:type_id>/', views.category_edit, name='category_edit'),
        path('delete/<int:type_id>/',
             views.category_delete, name='category_delete'),
        path('delete_all/',
             views.delete_all_categories, name='category_delete_all'),
        path('add/', views.add_category, name='add_category'),
    ])),

    path('subcategories/', include([
        path('',
             views.subcategory_list, name='subcategory_list'),
        path('edit/<int:subcategory_id>/', views.subcategory_edit,
             name='subcategory_edit'),
        path('delete/<int:subcategory_id>/',
             views.subcategory_delete, name='subcategory_delete'),
        path('add/', views.add_subcategory, name='add_subcategory'),
    ])),
]
