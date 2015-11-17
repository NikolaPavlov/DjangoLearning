from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {'questions': questions}
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/detail.html'
    context = {'question': question}
    return render(request, template, context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/results.html'
    context = {'question': question}
    return render(request, template, context)


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question form
        template = 'polls/detail.html'
        context = {
            'question': q,
            'error_message': 'You didnt select a choice'
        }
        return render(request,
                        template,
                        context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))
