from django.shortcuts import render

# Create your views here.
def student(request):
    context = {}
    return render(request, 'student.html', context=context)

def host(request):
    context = {}
    return render(request, 'host.html', context=context)


