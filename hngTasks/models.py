from django.db import models

# Create your models here.
class HNGSLack(models.Model):
    slack_name = models.CharField(max_length=250)
    current_day = models.CharField(null=True, blank=True, max_length=100)
    utc_time = models.DateTimeField(auto_now=True)
    track = models.CharField(max_length=200)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
    status_code = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'my name is {self.slack_name} and track is {self.track}'