from django.shortcuts import render, get_object_or_404


def sntc(request):
    return render(request, 'sntc.html', {})



def aero_modelling(request):
    return render(request, 'aero_modelling.html', {})
	
	
def astronomy(request):
    return render(request, 'astronomy.html', {})
	

def robotics(request):
    return render(request, 'robotics.html', {})

	
def cops(request):
    return render(request, 'cops.html', {})

	
	
def green(request):
    return render(request, 'green.html', {})
	

def cef(request):
    return render(request, 'cef.html', {})
	
	
def sae_collegiate(request):
    return render(request, 'sae_collegiate.html', {})


def troc(request):
    return render(request, 'troc.html', {})

def auv(request):
    return render(request, 'auv.html', {})

def vocowsa(request):
    return render(request, 'vocowsa.html', {})

def baja(request):
    return render(request, 'baja.html', {})

def technex(request):
    return render(request, 'technex.html', {})

