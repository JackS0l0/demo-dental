from django.shortcuts import render
def index(request):
    data={
        'title':'BrightDent Studio',
    }
    return render(request,'index.html',data)