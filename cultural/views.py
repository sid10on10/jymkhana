from django.shortcuts import render, get_object_or_404

def cultural(request):
    return render(request, 'cultural.html', {})
	
	
def fac(request):
    return render(request, 'fac.html', {})
	

def imc(request):
    return render(request, 'imc.html', {})
	
		
	
def lit(request):
    return render(request, 'lit.html', {})
	

def masq(request):
    return render(request, 'masq.html', {})
	
	
def quiz(request):
    return render(request, 'quiz.html', {})
	




	
