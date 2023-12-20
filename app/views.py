from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context
from django.shortcuts import render, redirect
from app.models import productor,ingreso,envase


def index(request):
    return render(request, 'index.html')

def mas_info(request):
    return render(request, 'masinfo.html')

def productores(request):
    productores = productor.objects.all()
    data={'productores':productores}
    return render(request, 'productores.html', data)

def ingresos(request):
    ingresos = ingreso.objects.all()
    envases = envase.objects.all()
    productores = productor.objects.all()
    i={ 'ingresos':ingresos,
        'envases':envases,
        'productores':productores
    }
    return render(request, 'ingresos.html', i)

def nuevo_ingreso(request):
    id_env=request.POST['envase']
    env=envase.objects.get(id=id_env)
    cantidad=request.POST['cant']
    id_prod=request.POST['productor']
    prod=productor.objects.get(id=id_prod)
    fecha=request.POST['fecha']
    i = ingreso.objects.create(Envase=env,Cantidad=cantidad, Productor=prod, Fecha=fecha)
    return redirect('ingresos')

def retiros(request):
    ret = ingreso.objects.all()
    return render(request, 'retiros.html',{'retiros':ret})

def retirar(request, cod):
    i = ingreso.objects.get(id=cod)
    i.Retirado = 'True'
    i.save()
    return redirect('ingresos')