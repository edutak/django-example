from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Thumbnail
# ResizeToFill : 300*300 자르는 것(crop)
# ResizeToFit : 가장 긴 곳(너비/높이)을 300으로 맞추고, 비율에 맞춰서

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 원본 저장 + 자른 것을 활용 : ImageSpecField + source
    image = models.ImageField()
    # DB 저장 X, 호출하게되면, 잘라서 표현
    image_thumbnail = ImageSpecField(source='image',
                          processors=[Thumbnail(300, 300)],
                          format='JPEG',
                          options={'quality': 60})
    # 원본 잘라서 저장 : ProcessedImageField
    # image = ProcessedImageField(
    #                       processors=[ResizeToFill(100, 50)],
    #                       format='JPEG',
    #                       options={'quality': 60})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

