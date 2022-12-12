from django.forms import ModelForm
from todo_app.models import Task, Comment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args, **kwargs)

        self.instance.task = task