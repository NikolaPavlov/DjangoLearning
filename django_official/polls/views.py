from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    # questions = Question.objects.all()
    template = 'index.html'
    context = {'questions': questions}
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse('Your looking at results of ' + question_id)


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question form
        return render(request, 'detail.html',
                      {'question': p,
                       'error_message': 'You didnt select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
