from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Choice, Question
from django.views import generic


# Create your views here.
class IndexViews(generic.ListView):
    model = Question
    context_object_name = "latest_question_list"
    template_name = "polls/index.html"
    queryset = Question.objects.order_by("-pub_date")[:5]


class DetailViews(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsViews(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a coice"},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
