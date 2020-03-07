from django.db import models

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	author=models.CharField(default='author',max_length=60)
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=60)
	body = models.TextField()
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return unicode("%s: %s" % (self.post, self.body[:60]))

class Contact(models.Model):
	name=models.CharField(max_length=60)
	subject=models.CharField(max_length=60)
	message=models.TextField()
	def __unicode__(self):
		return self.subject

class REG(models.Model):
        username=models.CharField(max_length=100)
        email=models.CharField(max_length=100)
        password=models.CharField(max_length=100)
        hint=models.CharField(max_length=100)
        date=models.DateField()

        def __unicode__(self):
                return """Username: %s saved, 
                        please wait for approval""" % (self.username)


