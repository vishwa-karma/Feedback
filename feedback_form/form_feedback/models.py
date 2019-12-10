from django.db import models

# Create your models here.
class FeedBackForm(models.Model):
    name = models.CharField(verbose_name='Name of the Participant', max_length=100, default='anonymous', blank=True)
    e_id = models.CharField(verbose_name='Participant ID', max_length=50, blank=True)
    email = models.EmailField(verbose_name='Email ID', blank=True)

    achieved = models.IntegerField(verbose_name='Were Course Objectives Achieved?', default=3)
    defined = models.IntegerField(verbose_name='Were the Objectives well defined?', default=3)

    appropriate = models.IntegerField(verbose_name='Was the Course Content appropriate?', default=3)
    simplicity =  models.IntegerField(verbose_name='Was the content simple or complex?', default=3)
    clarity = models.IntegerField(verbose_name='Was the content fragmented/unclear or clear?', default=3)
    volume = models.IntegerField(verbose_name='Was the content not enough or too much?', default=3)

    discuss = models.IntegerField(verbose_name='Did the Trainer allow Sufficient Discussion?', default=2)
    participate = models.IntegerField(verbose_name='Did the Trainer encourage participation?', default=3)
    ideas = models.IntegerField(verbose_name='Did the Trainer help bring out new group Ideas?', default=3)
    again = models.IntegerField(verbose_name='Would you accept this Trainer again?', default=3)

    liked = models.TextField(blank=True,)
    disliked = models.TextField(blank=True)

    def __str__(self):
        return self.name