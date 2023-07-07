from django.shortcuts import render
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:        
        form = Registro()
    return render(request, 'core/registro.html', {'form':form})

def home(request):
    plantas = Producto.objects.all()
    return render(request, 'core/index.html', {'plantas':plantas})

def catalogo(request):
    plantas = Producto.objects.all()
    return render(request, 'core/catalogo.html', {'plantas':plantas})

def logout(request):
    return logout_then_login(request, login_url="login")

def limpiar(request):
    request.session.flush()
    plantas = Producto.objects.all()
    return render(request, 'core/index.html', {'plantas':plantas})

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for c in carro:
        if c[0] == codigo:
            c[2] = c[2] + 1
            c[5] = c[2] * c[1]
            break
    else:
        carro.append([codigo, producto.precio, 1, producto.imagen, producto.descripcion, producto.precio])  
    request.session["carro"] = carro
    plantas = Producto.objects.all()
    return render(request, 'core/index.html', {'plantas':plantas})
    

def carrito(request):
    carro = request.session.get("carro",[])
    return render(request, 'core/carrito.html',{"carro":carro})


def droptocar(request, codigo):
    carro = request.session.get("carro",[])
    for c in carro:
        if c[0] == codigo:
            carro.remove(c)
            break
    request.session["carro"] = carro 
    return render(request, 'core/carrito.html',{"carro":carro})


def comprar(request):
    carro = request.session.get("carro", [])
    total = 0
    for c in carro:
        total += c[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    # Guardamos cada producto en la tabla detalle
    for c in carro:
        producto= Producto.objects.get(codigo=c[0])
        detalle = Detalle()
        detalle.venta = venta
        detalle.producto = Producto.objects.get(codigo=c[0])
        detalle.cantidad = c[2]
        detalle.precio = c[1]
        detalle.total = c[5]
        detalle.save()
        producto.stock=producto.stock - c[2]
        producto.save()
    request.session["carro"] = []
    return redirect(to="carrito")

def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    compras = Venta.objects.filter(cliente=request.user)
    return render(request, 'core/historial.html', {"compras":compras})
