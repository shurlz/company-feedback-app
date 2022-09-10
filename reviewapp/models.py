from django.db import models

# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=10)

    class Meta:
        ordering = ['tag_name']

class companyReview(models.Model):
    company_name = models.CharField(max_length=15)
    review = models.TextField()
    worked_here = models.BooleanField(default=True)
    date_posted = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)

    class Meta:
        ordering = ['-date_posted']
        