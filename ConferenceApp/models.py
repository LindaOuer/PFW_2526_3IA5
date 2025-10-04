from django.db import models
from django.core.validators import MinLengthValidator, FileExtensionValidator
from userApp.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Conference(models.Model):
    THEME_CHOICES = [
    ("AI", "Computer Science & Artificial Intelligence"),
    ("SE", "Science & Engineering"),
    ("SSE", "Social Sciences & Education"),
    ("INT", "Interdisciplinary Themes"),
    ]
    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    theme = models.CharField(max_length=50, choices=THEME_CHOICES)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(validators=[MinLengthValidator(30, "Description must be at least 30 characters long.")])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def clean (self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date cannot be earlier than start date.")
    
class Submission(models.Model):
    STATUS_CHOICES = [
    ("submitted", "Submitted"),
    ("under_review", "Under Review"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
    ]

    submission_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    keywords = models.TextField()
    paper = models.FileField(
        upload_to="papers/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    submission_date = models.DateField(auto_now_add=True)
    payed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="submissions")
    
class OrganizingCommittee(models.Model):
    ROLE_CHOICES = [
    ("chair", "Chair"),
    ("co-chair", "Co-chair"),
    ("committee", "Organizing Committee Member"),
]
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name="committee_members")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="committees")
    committee_role = models.CharField(max_length=100,choices=ROLE_CHOICES,default="comite")
    date_joined = models.DateField(auto_now_add=True)
