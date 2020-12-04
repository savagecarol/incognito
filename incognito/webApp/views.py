from django.shortcuts import render
from  services.textformatting import formatting


def index(request):
    formatting('''
    hello i am alanakr
    thi is me working
    ''')
    return render(request, 'index.html')
