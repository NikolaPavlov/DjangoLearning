from django.shortcuts import render
# from django.http import HttpResponse

from .models import Question


# Create your views here.
def index(request):
    latests_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latests_question_list': latests_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """TODO: Docstring for detail.

    :request: TODO
    :question_id: TODO
    :returns: TODO

    """
    pass


def results(request, question_id):
    """TODO: Docstring for results.

    :request: TODO
    :question_id: TODO
    :returns: TODO

    """
    pass


def vote(request, question_id):
    """TODO: Docstring for vote.

    :request: TODO
    :question_id: TODO
    :returns: TODO

    """
    pass
