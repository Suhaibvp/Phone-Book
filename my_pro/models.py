from django.db import models







class userdetailss(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    occupation=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    umob=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    pincode=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    image=models.CharField(max_length=200)


class cadd(models.Model):
    cname=models.CharField(max_length=200)
    mob=models.CharField(max_length=200)
    cemail=models.CharField(max_length=200)
    cplace=models.CharField(max_length=200)
    image=models.CharField(max_length=200)


