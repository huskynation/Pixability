from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.
class SignUp(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    udpated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.email)

class PDFUpload(models.Model):
	file_upload = models.FileField(upload_to='/Users/INKQWIRE/Desktop/skillshare/upload')
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)

	# class Meta:
	# 	model = PDFUpload


