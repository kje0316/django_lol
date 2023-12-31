from django.db import models
import importlib
from django.core import validators


# Create your models here
class User(models.Model):
    id = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)


class Champions(models.Model):
    champion = models.CharField(primary_key=True, max_length=255)
    line = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=100, null=True)
    CC = models.CharField(max_length=512, null=True)

    @property
    def image(self):
        return self.champion_tip_set.first().image_url


class Champion_rate(models.Model):
    champion = models.ForeignKey(Champions, primary_key=True, on_delete=models.CASCADE)
    line = models.CharField(max_length=100)
    win_rate = models.CharField(max_length=100)
    pick_rate = models.CharField(max_length=100)
    ban_rate = models.CharField(max_length=100)


class Champion_story(models.Model):
    champion = models.ForeignKey(Champions, primary_key=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=512)
    text = models.TextField()
    story = models.TextField()


class champion_tip(models.Model):
    champion = models.ForeignKey(Champions, primary_key=True, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=512)
    enemy_tips = models.TextField()
    ally_tips = models.TextField()


class Champion_counter(models.Model):
    # id = models.AutoField(primary_key=True, null=False)
    champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
    counter_name = models.CharField(max_length=512)
    win = models.CharField(max_length=512)

    @property
    def image(self):
        return self.champion.image


class champion_skill_name(models.Model):
    champion = models.ForeignKey(Champions, primary_key=True, on_delete=models.CASCADE)
    passive_name = models.CharField(max_length=512)
    Q_name = models.CharField(max_length=512)
    W_name = models.CharField(max_length=512)
    E_name = models.CharField(max_length=512)
    R_name = models.CharField(max_length=512)


class champion_skill_img_text(models.Model):
    champion = models.ForeignKey(Champions, primary_key=True, on_delete=models.CASCADE)
    cham_img = models.CharField(max_length=512)
    passive_img = models.CharField(max_length=512)
    q_img = models.CharField(max_length=512)
    w_img = models.CharField(max_length=512)
    e_img = models.CharField(max_length=512)
    r_img = models.CharField(max_length=512)
    passive = models.CharField(max_length=512)
    Q = models.CharField(max_length=512)
    W = models.CharField(max_length=512)
    E = models.CharField(max_length=512)
    R = models.CharField(max_length=512)


class Review(models.Model):
    champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.FloatField()
    likes = models.FloatField()


class WordCloud(models.Model):
    champion = models.ForeignKey(Champions, on_delete=models.CASCADE)
    img = models.ImageField()


class Comment(models.Model):
    content = models.CharField(
        "댓글 입력",
        max_length=255,
        validators=[validators.MinLengthValidator(3, "최소 세 글자 이상은 입력해주셔야 합니다.")],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    champion = models.ForeignKey(
        Champions,
        #   related_name='comment_set',
        on_delete=models.SET_NULL,
        null=True,
    )
    comment_id = models.AutoField(primary_key=True)
