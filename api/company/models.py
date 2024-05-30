import uuid

from django.db import models


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField()
    founded_date = models.DateField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, related_name='measures', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    date_recorded = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.value}"


class KPI(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, related_name='kpis', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target_value = models.FloatField()
    actual_value = models.FloatField()
    date_measured = models.DateField()

    def __str__(self):
        return f"{self.name} - Target: {self.target_value}, Actual: {self.actual_value}"


class Control(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, related_name='controls', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    last_reviewed = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.status}"
