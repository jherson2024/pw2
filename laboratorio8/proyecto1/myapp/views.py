from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template

def pagina_principal(request):
    return render(request, "index.html")

def render_pdf_view(request):
    context = {
        "content": "",
    }
    template_path = 'index.html'
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename='archivo.pdf'"
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response, encoding="utf-8")
    if pisa_status.err:
        return HttpResponse("Hubo errores al generar el PDF: %s" % html)
    return response