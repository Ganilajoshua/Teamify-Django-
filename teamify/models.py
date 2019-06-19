from django.conf import settings
from django.db import models
from django.utils import timezone


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    task_assign_to = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.task_name

class subTask(models.Model):
    subtask_id = models.AutoField(primary_key=True)
    subtask_creator = models.ForeignKey(Task,to_field='task_id', db_column="task_id", on_delete=models.CASCADE)
    subtask_name = models.CharField(max_length=200)
    subtask_description = models.TextField()
    subtask_assign_to = models.IntegerField()
    subtask_created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.subtask_published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subtask_name