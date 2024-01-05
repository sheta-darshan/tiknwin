from django.contrib import admin
from .models import Sports, Team, Match, Prediction, User, Leaderboard, Notification, Comment, UserActivity, Reward, UserSubscription


# Register your models here.
admin.site.register(Sports)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Prediction)
admin.site.register(User)
admin.site.register(Leaderboard)
admin.site.register(Notification)
admin.site.register(Comment)
admin.site.register(UserActivity)
admin.site.register(Reward)
admin.site.register(UserSubscription)
