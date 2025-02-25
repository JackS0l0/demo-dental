from django.shortcuts import render
from .models import MainTexts,Specialty,HeaderSlider
def index(request):
    data={
        'title':'BrightDent Studio',
        'maintexts':MainTexts.objects.all(),
        'specialties':Specialty.objects.all()[0:4],
        'headerslider':HeaderSlider.objects.all(),
    }
    return render(request,'index.html',data)