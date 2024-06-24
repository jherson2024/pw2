from django.urls import path
from .views import PersonaListView, PersonaDetailView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView, PersonaQueryView

app_name = 'personas'

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona-list'),
    path('persona/<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('persona/new/', PersonaCreateView.as_view(), name='persona-create'),
    path('persona/<int:pk>/edit/', PersonaUpdateView.as_view(), name='persona-update'),
    path('persona/<int:pk>/delete/', PersonaDeleteView.as_view(), name='persona-delete'),
    path('query/', PersonaQueryView.as_view(), name='persona-query'),
]