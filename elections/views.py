from django.http import HttpResponse
from django.shortcuts import render

from .models import Candidate

# Create your views here.


def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}  # context에 모든 후보에 대한 정보를 저장
    # context로 html에 모든 후보에 대한 정보를 전달
    return render(request, 'elections/index.html', context)
