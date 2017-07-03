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
	

def clubofeconomicsandfinance(request):
    return render(request, 'clubofeconomicsandfinance.html', {})
	
	
def sae_collegiate(request):
    return render(request, 'sae_collegiate.html', {})


def troc(request):
    return render(request, 'troc.html', {})

	



