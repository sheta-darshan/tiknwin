from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Sports(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)

    # Additional information (optional)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    # Basic information
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)

    # Additional information (optional)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    home_stadium = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)

    # Flag image
    flag_image = models.ImageField(upload_to='media/team_flags/', null=True, blank=True)

    # Relationships
    sports = models.ManyToManyField('Sports', related_name='teams')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    # Teams playing in the match
    home_team = models.ForeignKey('Team', related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey('Team', related_name='away_matches', on_delete=models.CASCADE)

    # Match details
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    result = models.CharField(max_length=50, blank=True, null=True)

    # Additional information (optional)
    description = models.TextField(blank=True)

    # Link to Sports
    sports = models.ForeignKey('Sports', related_name='matches', on_delete=models.CASCADE, null=True, blank=True)


    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} - {self.date_time}"

class Prediction(models.Model):
    # User who made the prediction
    user = models.ForeignKey('user', on_delete=models.CASCADE)

    # Match for which the prediction is made
    match = models.ForeignKey('Match', on_delete=models.CASCADE)

    # Predicted result
    predicted_team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    

    # Additional information (optional)
    prediction_comment = models.TextField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.user.username}'s Prediction for {self.match}"

class User(AbstractUser):
    # Additional fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    # Contact Information
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    
    # Additional Personal Information
    bio = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    
    # Employment Information
    occupation = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    
    # Additional Settings
    receive_newsletter = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField('auth.Group',blank=True,related_name='user_groups')

    # Unique related_name for user_permissions
    user_permissions = models.ManyToManyField('auth.Permission',blank=True,related_name='user_user_permissions')

    def __str__(self):
        return self.username
    

class Leaderboard(models.Model):
    user = models.OneToOneField('user', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Points: {self.points}"
    

class Notification(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message}"
    

class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    prediction = models.ForeignKey('Prediction', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text}"
    

class UserActivity(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"
    

class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points_required = models.IntegerField()

    def __str__(self):
        return self.name
    
class UserSubscription(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.plan_name}"

