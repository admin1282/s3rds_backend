from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
import boto3
# Create your models here.
class Profile(models.Model):
    image = models.FileField(upload_to=settings.PROFILE, blank=True, null=True)
    image2 = models.FileField(upload_to=settings.PROFILE2, blank=True, null=True)
    image3 = models.ImageField(upload_to=settings.PROFILE3, blank=True, null=True)


    # Signal receiver function to delete file from S3
    @receiver(post_delete)
    def delete_file_from_s3(sender, instance, **kwargs):
        if hasattr(instance, 'image2') and instance.image2:  # Check if the model has a 'file' field
            s3 = boto3.client('s3',
                              aws_access_key_id='AKIA4MTWHB5L3CE4FVHS',
                              aws_secret_access_key='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')
            s3.delete_object(Bucket='s3rdsbackendbucket', Key=str(instance.image2))