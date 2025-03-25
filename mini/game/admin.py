from django.contrib import admin

# Register your models here.
from .models import Content,Game,Quiz,Reward,Use1,UserReward,UserProgress,UserProfile,Question,Notification,Feedback,Answer
admin.site.register(Content)
admin.site.register(Game)
admin.site.register(Quiz)
admin.site.register(Reward)
admin.site.register(Use1)
admin.site.register(UserReward)
admin.site.register(UserProgress)
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Notification)
admin.site.register(Feedback)
admin.site.register(Answer)