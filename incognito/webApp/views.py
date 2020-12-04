from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        print(content)
    return render(request, 'index.html')
