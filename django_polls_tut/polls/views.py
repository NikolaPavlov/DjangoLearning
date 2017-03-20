from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', locals())


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choices.all()
    return render(request, 'polls/detail.html', locals())


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choices.all()
    return render(request, 'polls/results.html', locals())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question.id)
        # return redirect(reverse('polls:results', args=[question.id]))
