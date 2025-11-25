from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.views.decorators.http import require_POST


def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def create_task(request):
    # Placeholder for task creation logic
    return render(request, "create_task.html")


@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("index")


@require_POST
def task_toggle_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("index")
