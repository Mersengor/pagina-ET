from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", home, name="home"),    
    path("login", LoginView.as_view(template_name="core/login.html"), name="login"),    
    path("logout", logout, name="logout"),   
    path("registro", registro, name="registro"),
    path("home/<codigo>", addtocar, name="addtocar"),
    path("droptocar/<codigo>", droptocar, name="droptocar"),
    path("limpiar", limpiar, name="limpiar"),
    path("carrito", carrito, name="carrito"),
    path("historial", historial, name="historial"),
    path("comprar", comprar, name="comprar"),
    path("catalogo", catalogo, name="catalogo"),
    ]
