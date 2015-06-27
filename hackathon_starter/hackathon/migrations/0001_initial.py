# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropboxProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dropbox_user_id', models.CharField(max_length=100)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('access_token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fb_user_id', models.CharField(max_length=100)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('profile_url', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoursquareProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foursquare_id', models.CharField(max_length=100)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('access_token', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GithubProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('github_user', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=200)),
                ('scopes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('google_user_id', models.CharField(max_length=100)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('access_token', models.CharField(max_length=100)),
                ('profile_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instagram_user', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linkedin_user', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MeetupToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('area', models.CharField(default=b'Johannesburg', max_length=140)),
                ('phone_number', models.CharField(default=b'000-000-0000', max_length=140)),
                ('talent', models.CharField(default=b'', max_length=140)),
                ('rating', models.IntegerField(default=b'-1', max_length=2)),
                ('rating_ontime', models.IntegerField(default=b'-1', max_length=2)),
                ('rating_value', models.IntegerField(default=b'-1', max_length=2)),
                ('rating_reliability', models.IntegerField(default=b'-1', max_length=2)),
                ('rating_qualit', models.IntegerField(default=b'-1', max_length=2)),
                ('business_name', models.CharField(default=b'', max_length=140)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MerchantProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('merchant', models.OneToOneField(to='hackathon.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oauth_token', models.CharField(max_length=200)),
                ('oauth_secret', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='TumblrProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tumblr_user', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=200)),
                ('access_token_secret', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_user', models.CharField(max_length=200)),
                ('oauth_token', models.CharField(max_length=200)),
                ('oauth_token_secret', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('area', models.CharField(default=b'Johannesburg', max_length=140)),
                ('phone_number', models.CharField(default=b'000-000-0000', max_length=140)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to='hackathon.User')),
            ],
        ),
        migrations.AddField(
            model_name='twitterprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='tumblrprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='linkedinprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='instagramprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='googleprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='githubprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='foursquareprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='facebookprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
        migrations.AddField(
            model_name='dropboxprofile',
            name='user',
            field=models.ForeignKey(to='hackathon.User'),
        ),
    ]
