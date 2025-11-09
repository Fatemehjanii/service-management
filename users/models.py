from django.db import models
class UserSanay(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('tester', 'Tester'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    experience_years = models.IntegerField()
    skills = models.TextField()
    join_date = models.DateField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.full_name