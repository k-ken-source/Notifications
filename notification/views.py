from django.shortcuts import render

def Home(request):
    context = {}
    context['obj'] = 'this is rendering object'
    return render(request,'notification/index.html',context)


