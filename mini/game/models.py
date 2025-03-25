from django.db import models
from django.contrib.auth.models import AbstractUser

class Use1(models.Model):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='use1_set',  # Change related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        verbose_name=('groups'),
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='use1_permission_set',  # Change related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

class UserProfile(models.Model):
    user = models.OneToOneField(Use1, on_delete=models.CASCADE, related_name='profile')
    school_name = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Quiz(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1=models.CharField(max_length=255, default='Default Option 1')
    option2=models.CharField(max_length=255, default='Default Option 2')
    option3=models.CharField(max_length=255, default='Default Option 3')
    option4=models.CharField(max_length=255, default='Default Option 4')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.answer_text
  
class UserProgress(models.Model):
    user = models.ForeignKey(Use1, on_delete=models.CASCADE, related_name='progress')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_progress')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='user_progress')
    score = models.IntegerField()
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

class Reward(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserReward(models.Model):
    user = models.ForeignKey(Use1, on_delete=models.CASCADE, related_name='rewards')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='user_rewards')
    earned_at = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    content_type = models.CharField(max_length=50)  # e.g., article, video, infographic
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    user = models.ForeignKey(Use1, on_delete=models.CASCADE, related_name='feedback')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='feedback')
    feedback_text = models.TextField()
    rating = models.IntegerField()  # e.g., 1 to 5 stars
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    user = models.ForeignKey(Use1, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
