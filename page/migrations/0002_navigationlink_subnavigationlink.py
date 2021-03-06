# Generated by Django 2.1.7 on 2019-03-06 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('display_order', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.SitePage')),
            ],
            options={
                'verbose_name': 'Navigation Link',
                'verbose_name_plural': 'Navigation Links',
                'ordering': ('display_order', 'name'),
            },
        ),
        migrations.CreateModel(
            name='SubNavigationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('display_order', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page.SitePage')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
                'ordering': ('display_order', 'name'),
            },
        ),
    ]
