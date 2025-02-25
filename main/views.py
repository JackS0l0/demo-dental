from django.shortcuts import render
from .models import MainTexts,Specialty
def index(request):
    data={
        'title':'BrightDent Studio',
        'maintexts':MainTexts.objects.all(),
        'specialties':Specialty.objects.all()[0:4],
    }
    return render(request,'index.html',data)