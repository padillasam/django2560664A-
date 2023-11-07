from django.shortcuts import render
from . models import Aprendiz

# Create your views here.
# def listaaprendices(request):
#     return render(request,'listaaprendices.html')

def listaaprendices(request):
    get_aprendices=Aprendiz.objects.all()
    data={
        'get_aprendices':get_aprendices
    }
    return render(request, 'listaaprendices.html',data)
