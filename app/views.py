from django.shortcuts import render

# Create your views here.
def einstein(request):
    return render(request,'einstein.html')

def sun(request):
    return render(request,'sun.html')
