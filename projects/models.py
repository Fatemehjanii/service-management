from django.db import models
from users.models import UserSanay


class Project(models.Model):
    STATUS_CHOICES = [
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    CATEGORY_CHOICES = [
        ('web_development', 'Web Development'),
        ('app_development', 'Application Development'),
        ('ai', 'Artificial Intelligence'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web_development')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_do')
    owner = models.ForeignKey(UserSanay, on_delete=models.PROTECT)
    members = models.ManyToManyField(UserSanay, related_name='projects', blank=True)

    def __str__(self):
        return self.name