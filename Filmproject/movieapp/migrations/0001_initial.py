# Generated by Django 2.1.2 on 2019-04-03 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=64)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('content', models.TextField(null=True)),
                ('releasedate', models.DateField()),
                ('actor', models.CharField(max_length=30)),
                ('actress', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
                ('director', models.CharField(max_length=30, null=True)),
                ('producer', models.CharField(max_length=30, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
        ),
    ]
