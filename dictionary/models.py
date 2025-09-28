from django.db import models

class NewWord(models.Model):
    name = models.CharField(verbose_name='სიტყვა ინგლისურად', max_length=50)
    translate = models.CharField(verbose_name='თარგმანი ინგლისურად', max_length=50)
    Adjective = models.CharField(verbose_name='ზედსართავი სახელი', max_length=50)
    noun = models.CharField(verbose_name='არსებითი სახელი', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)



class Text(models.Model):
    name = models.CharField(verbose_name='სიტყვა ინგლისურად', max_length=50)
    text = models.TextField(verbose_name='ტექსტი', max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)