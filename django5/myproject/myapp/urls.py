from django.urls import path
from . import views

urlpatterns = [
    # path('', views.pagina_principal, name='home'),
    path('', PersonaListView.as_view(), name='persona-list'),
    path('<int:pk>/',PersonaDetailView.as_view(),name='persona-detail'),
    path('create/',PersonaCreateView.as_view(),name='persona-create'),
    path('<int:pk>/update',PersonaUpdateView.as_view(),name='persona-update'), 
    path('<int:pk>/delete',PersonaDeleteView.as_view(),name='persona-delete'), 
]