from django.shortcuts import render
# Create your views here.
def filter(request):
    d={'data':'hai how Are YoU'}
    return render(request,'filter.html',d)