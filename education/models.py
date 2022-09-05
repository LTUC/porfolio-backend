from django.db import models
from django.contrib.auth import get_user_model


class Degree(models.Model):
    degree = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.degree

class Organization(models.Model):
    organization = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.organization


class Education(models.Model):
    user = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.CASCADE, related_name="+")
    degree = models.ForeignKey(Degree, blank=False, null=False, on_delete=models.CASCADE, related_name="+")
    organization = models.ForeignKey(Organization, blank=False, null=False, on_delete=models.CASCADE, related_name="+")
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    current_student = models.BooleanField()
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.degree} - {self.organization}"