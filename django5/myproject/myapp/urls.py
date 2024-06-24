from django.urls import path
from . import views

urlpatterns = [
    # path('', views.pagina_principal, name='home'),
    path('', PersonaListView.as_view(), name='persona-list'),
    path('<int:pk>/',PersonaDetailView.as_view(),name='persona-detail'),
    path('create/',PersonaCreateView.as_view(),name='persona-create'),
]