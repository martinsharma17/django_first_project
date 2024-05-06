from django.db import models
# python manage.py makemigrations
# python manage.py migrate
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=50)
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactInformation(models.Model):
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.address1

class Services(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length= 300)
    post = models.CharField(max_length= 300)
    image = models.ImageField(upload_to='media',null = True)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.TextField()
    body = models.TextField()
    full_body = models.TextField()
    category = models.CharField(max_length=500)
    name = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.name






