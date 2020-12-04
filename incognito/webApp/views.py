from django.shortcuts import render
from  services.textformatting import formatting


def index(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        formatting(content)
    return render(request, 'index.html')
