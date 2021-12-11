from django.db import models

state_choices = [
    ("draft" ,"draft"),
    ("active" ,"active"),
    ("done" ,"done"),
    ("archived" ,"archived")
]

# Create your models here.
class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(null = False)
    state = models.CharField(max_length=50, choices=state_choices, default='draft')

    def __Str__(self):
        return f"The task {self.id} {self.title} in the state {self.state}"