from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def ask(request):
    return render(request, 'data/ask.html')

@login_required
def res(request):
    return render(request, 'data/res.html')
