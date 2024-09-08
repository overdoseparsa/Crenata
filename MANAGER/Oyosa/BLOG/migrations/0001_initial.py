# Generated by Django 5.1 on 2024-09-07 19:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('is_active', models.BooleanField(verbose_name='is activate Category')),
                ('followers_katalog', models.ManyToManyField(related_name='followers_katalog_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='USER_FOLLOWING', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('Following', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_FOLLOWER', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='titlegroub')),
                ('uudi', models.UUIDField()),
                ('accounts', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('slug', models.SlugField(allow_unicode=True, max_length=250, unique_for_date='publish', verbose_name='slug')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(help_text='this is the user include', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='BLOG.category')),
            ],
            options={
                'verbose_name': 'Post',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title media')),
                ('is_ruls', models.BooleanField()),
                ('path', models.FileField(upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BLOG.post', verbose_name='Post')),
            ],
            options={
                'ordering': ['post'],
            },
        ),
        migrations.CreateModel(
            name='GroupLevelPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='titlegroub')),
                ('uudi', models.UUIDField()),
                ('posts', models.ManyToManyField(to='BLOG.post')),
            ],
        ),
        migrations.CreateModel(
            name='Commants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TEXT', models.TextField(max_length=1000, verbose_name='text')),
                ('like', models.BigIntegerField()),
                ('dilike', models.BigIntegerField()),
                ('report', models.CharField(max_length=155)),
                ('media', models.FileField(upload_to='')),
                ('type_commant', models.CharField(choices=[('PR', 'private'), ('PB', 'public')], default='PR', max_length=2, verbose_name='type of commant')),
                ('commented_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(help_text='this is the user include', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User off comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BLOG.post', verbose_name='Post')),
            ],
            options={
                'ordering': ['post'],
            },
        ),
        migrations.CreateModel(
            name='TAGS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tags', models.CharField(max_length=120, verbose_name='typeoff commant')),
                ('followings_len', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ManyToManyField(to='BLOG.post')),
                ('tags_followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transmisson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BigIntegerField(verbose_name='like')),
                ('dislike', models.BigIntegerField(verbose_name='dslike')),
                ('share', models.BigIntegerField(verbose_name='share')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BLOG.post', verbose_name='Post')),
            ],
            options={
                'ordering': ['post'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-author'], name='BLOG_post_author__7281f3_idx'),
        ),
        migrations.AddIndex(
            model_name='media',
            index=models.Index(fields=['post'], name='BLOG_media_post_id_c95b63_idx'),
        ),
        migrations.AddIndex(
            model_name='commants',
            index=models.Index(fields=['post'], name='BLOG_comman_post_id_05f3da_idx'),
        ),
        migrations.AddIndex(
            model_name='transmisson',
            index=models.Index(fields=['post'], name='BLOG_transm_post_id_56e0c6_idx'),
        ),
    ]
