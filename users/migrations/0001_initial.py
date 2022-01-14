# Generated by Django 4.0.1 on 2022-01-14 22:37

import django.core.validators
from django.db import migrations, models
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff')),
                ('is_promoted', models.BooleanField(default=False, help_text='To promote the user for special features, e.g. SmartFlow Demo & ...', verbose_name='Is Promoted')),
                ('company', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='company')),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
                ('zipcode', models.CharField(blank=True, error_messages={'max_length': 'Zipcodes are not more than 12 characters.'}, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{5,12}$')])),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('country', models.CharField(blank=True, max_length=25, null=True)),
                ('tel', models.CharField(blank=True, max_length=17, null=True, verbose_name='phone')),
                ('mobile', models.CharField(blank=True, max_length=17, null=True, verbose_name='mobile')),
                ('fax', models.CharField(blank=True, max_length=17, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_id', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True, verbose_name='website')),
                ('previous_visit', models.DateTimeField(blank=True, null=True)),
                ('current_visit', models.DateTimeField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]