from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista3(request):
    html= """
    <h1>Proyecto rama 2</h1>
    <p Style="color:green">Lorem ipsum es el texto que se usa <b>habitualmente en diseño gráfico en demostraciones <b> de tipografías o de borradores de diseño para probar el diseño visual antes de <br> insertar el texto final.</p>
"""
    return HttpResponse(html)

def vista4(request):
    html= """
    <h1>Proyecto rama 2 segunda vista</h1>
    <p Style="color:yellow">Lorem ipsum es el texto que se usa <b>habitualmente en diseño gráfico en demostraciones <b> de tipografías o de borradores de diseño para probar el diseño visual antes de <br> insertar el texto final.</p>
"""
    return HttpResponse(html)