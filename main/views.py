from django.shortcuts import render
from .models import MainTexts,Specialty,HeaderSlider,Reviews,Doctors,Servies
def index(request):
    data={
        'title':'BrightDent Studio',
        'maintexts':MainTexts.objects.all(),
        'specialties':Specialty.objects.all()[0:4],
        'headerslider':HeaderSlider.objects.all(),
        'reviews':Reviews.objects.all()[0:3],
        'doctors':Doctors.objects.all()[0:4],
        'servies':Servies.objects.all(),
    }
    return render(request,'index.html',data)