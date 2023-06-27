# board/models.py
from django.db import models
from django.conf import settings


class Feed(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feeds')
    # 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_feeds')
    
    # 싫어요
    # dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_feeds')


class Reaction(models.Model):
    content = models.CharField(max_length=200)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reactions')
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='reactions')


"""
u1 = User.objects.get(pk=1)

u1.like_feeds.add(f1)
f1.like_users.add(u1)

u1.like_feeds.remove(f1)
f1.like_users.remove(u1)

# u1이 작성한 피드들
u1.feeds.all()

# u1이 작성한 반응들
u1.reactions.all()

# u1이 좋아요 누른 피드들
u1.like_feeds.all()

# u1이 작성한 피드 중 1번째 피드에 달린 댓글(반응)들
u1.feeds.all()[0].reactions.all()

# u1이 좋아요 누른 피드중 마지막 피드의 좋아요 수
u1.like_feeds.all().last().like_users.count()
u1.like_feeds.last().like_users.count()

# u1이 반응한 피드들중 1번째 피드을 작성한 사용자가 좋아요 한 피드들
u1.reactions.first().author.like_feeds.all()


f2 = Feed.objects.get(pk=2)

# f2에 달린 반응 개수
f2.reactions.count()

# f2의 반응중 1번째 반응의 작성자가 작성한 피드들

f2.reactions.first().author.feeds.all()
"""