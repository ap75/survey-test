from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SurveyRes

def ask(request):
    return render(request, 'data/ask.html')

@login_required
def res(request):
    res = {
        'total': SurveyRes.objects.all().count(),
        'has_money': SurveyRes.objects.filter(has_money=True).count(),
        'is_generous': SurveyRes.objects.filter(is_generous=True).count(),
        'list': SurveyRes.objects.filter(is_generous=True)
    }
    return render(request, 'data/res.html', res)
