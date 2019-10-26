
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views

from apiclasses.views import ListView, DetailView, UpdateView,DeleteView,CreateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),


    path('api/list/', ListView.as_view()), #done 
    path('api/detail/<int:classroom_id>', DetailView.as_view()), #done 
    
    path('api/classrooms/<int:classroom_id>/delete/', DeleteView.as_view()), #done i think
    path('api/classrooms/<int:classroom_id>/update/', UpdateView.as_view()), #done i think
    

    path('api/classrooms/create/', CreateView.as_view()), #done i think
	

	path('api/login/', TokenObtainPairView.as_view()), #done i think

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


