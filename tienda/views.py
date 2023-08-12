from django.shortcuts import render
from tienda.models import Orden
# Create your views here.

def v_index(request):
    fecha_inicio = request.GET.get("fecha_inicio",None)
    fecha_fin = request.GET.get("fecha_fin",None)

    fecha_e_inicio = request.GET.get("fecha_inicio",None)
    fecha_e_fin = request.GET.get("fecha_fin",None)

    consulta = Orden.objects.all()

    if fecha_inicio is not None and fecha_fin is not None:
        consulta = Orden.objects.filter(fecha__range = (fecha_inicio, fecha_fin))

    context ={
        "ordenes": consulta
    }

    return render(request, "index.html", context)

