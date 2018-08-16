from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    '''
    The basic building block for the app. Users create projects: everything 
    else is attached to a project or one of its children
    '''
    title = models.TextField(null=True)
    description = models.TextField(null=True)
    users = models.ManyToManyField(User, through='ProjectRoles')
    queries = models.IntegerField(default=0)
    docs = models.IntegerField(default=0)
    reldocs = models.IntegerField(default=0)
    tms = models.IntegerField(default=0)

    def __str__(self):
      return self.title

class ProjectRoles(models.Model):

    ROLE_CHOICES = (
        ('OW', 'Owner'),
        ('AD', 'Admin'),
        ('RE', 'Reviewer'),
        ('VE', 'Viewer')
    )

    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)

    def __str__(self):
      return self.role
