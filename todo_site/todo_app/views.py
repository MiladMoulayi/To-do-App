from django.shortcuts import redirect, render
from django.views import View
from todo_app.models import Task, Comment, Tag
from todo_app.forms import TaskForm, CommentForm, TagForm

# Create your views here.

class HomeView(View):
    def get(self, request):
        tasks = Task.objects.all()
        task_form = TaskForm

        html_data = {
            'task_list': tasks,
            'form': task_form,
        }

        return render(
            request=request,
            template_name='index.html',
            context=html_data,
        )

    def post(self, request): 
        task_form = TaskForm(request.POST)
        task_form.save()

        return redirect('home')

class TaskDetailView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)

        comments = Comment.objects.filter(task=task)
        comment_form = CommentForm(task_object=task)

        tag = Tag.objects.filter(task=task)
        tag_form = TagForm(instance=task)

        html_data = {
            'task_object': task,
            'form': task_form,
            'comment_list': comments,
            'comment_form': comment_form,
            'tag_list': tag,
            'tag_form': tag_form,
        }

        return render(
            request=request,
            template_name='detail.html',
            context=html_data,
        )

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)

        if 'update' in request.POST:
            task_form = TaskForm(request.POST, instance=task)
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()
        elif 'add' in request.POST:
            comment_form = CommentForm(request.POST, task_object=task)
            comment_form.save()
            return redirect('task_detail', task_id)
        elif 'tag' in request.POST:
            tag_form = TagForm(request.POST, instance=task)
            tag_form.save(task=task)
            return redirect('task_detail', task_id)

        return redirect('home')