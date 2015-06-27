from django.db import models
from django.contrib.auth.models import User as OrigUser


class User(OrigUser):
    area = models.CharField(max_length=140, default='Johannesburg')
    phone_number = models.CharField(max_length=140, default='000-000-0000')


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Area(models.Model):
    name = models.CharField(max_length=140, default='Johannesburg')
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name


class Neighbourhood(models.Model):
    area = models.ForeignKey(Area)
    name = models.CharField(max_length=140, default='Parktown')
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name + self.area.name


class Merchant(OrigUser):
    place = models.ForeignKey(Neighbourhood)
    phone_number = models.CharField(max_length=140, default='000-000-0000')
    talent = models.CharField(max_length=140, default='')
    rating = models.IntegerField(default='-1')
    rating_ontime = models.IntegerField(default='-1')
    rating_value = models.IntegerField(default='-1')
    rating_reliability = models.IntegerField(default='-1')
    rating_quality = models.IntegerField(default='-1')
    business_name = models.CharField(max_length=140, default='')


class MerchantRating(models.Model):
    merchant = models.ForeignKey(Merchant)
    rating_ontime = models.IntegerField(default='-1')
    rating_value = models.IntegerField(default='-1')
    rating_reliability = models.IntegerField(default='-1')
    rating_quality = models.IntegerField(default='-1')
    user = models.ForeignKey(User)
    text = models.TextField(max_length=200)

    def __unicode__(self):
        return "Merchant: " + self.merchant.name + " - Avg Rating: " + str(self.calculate_average())

    def calculate_average(self):
        return (self.rating_ontime + self.rating_quality + self.rating_reliability + self.rating_value) / 4.0


class MerchantProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    merchant = models.OneToOneField(Merchant)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.merchant.username


class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class GithubProfile(models.Model):
    user = models.ForeignKey(User)
    github_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    scopes = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class TumblrProfile(models.Model):
    user = models.ForeignKey(User)
    tumblr_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class InstagramProfile(models.Model):
    user = models.ForeignKey(User)
    instagram_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class TwitterProfile(models.Model):
    user = models.ForeignKey(User)
    twitter_user = models.CharField(max_length=200)
    oauth_token = models.CharField(max_length=200)
    oauth_token_secret = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class LinkedinProfile(models.Model):
    user = models.ForeignKey(User)
    linkedin_user = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.user)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class MeetupToken(models.Model):
    # user = models.ForeignKey(User)
    access_token = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.access_token)


class FacebookProfile(models.Model):
    user = models.ForeignKey(User)
    fb_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)


class GoogleProfile(models.Model):
    user = models.ForeignKey(User)
    google_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)


class DropboxProfile(models.Model):
    user = models.ForeignKey(User)
    dropbox_user_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)


class FoursquareProfile(models.Model):
    user = models.ForeignKey(User)
    foursquare_id = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    access_token = models.CharField(max_length=100)
