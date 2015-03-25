# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from vote.models import *

def vote_view(request):
	if request.method == 'GET':
		n =	Candidates.objects.all()
		m = Person.objects.all()
		return render_to_response('vote.html', {'cand_list':n, 'person_list':m})

def result_view(request):
	if request.method == 'POST':
		choiceVal = request.POST.get('cand')
		selChoice = Candidates.objects.get(personID=choiceVal)
		selChoice.cnt += 1
		selChoice.save()
		n =	Candidates.objects.all()
		m = Person.objects.all()
		return render_to_response('view.html', {'cand_list':n, 'person_list':m})