from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('pdf/',views.render_pdf_view, name='render_pdf'),
]