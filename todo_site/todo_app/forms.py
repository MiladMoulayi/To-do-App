from django.forms import ModelForm
from todo_app.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description']