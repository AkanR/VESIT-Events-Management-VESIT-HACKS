# Generated by Django 3.1.7 on 2021-04-03 18:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_assigned', models.CharField(choices=[('STUDENT', 'STUDENT'), ('PRINCIPAL', 'PRINCIPAL'), ('MCA_HOD', 'PRINCIPAL'), ('CMPN_HOD', 'CMPN_HOD'), ('INFT_HOD', 'INFT_HOD'), ('INST_HOD', 'INST_HOD'), ('AIML_HOD', 'AIML_HOD'), ('COUNCIL_INCHARGE', 'COUNCIL_INCHARGE'), ('CSI_STAFF', 'CSI_STAFF'), ('IEEE_STAFF', 'IEEE_STAFF'), ('ISA_STAFF', 'ISA_STAFF'), ('ISTE_STAFF', 'ISTE_STAFF'), ('VESLIT_STAFF', 'VESLIT_STAFF'), ('ECELL_STAFF', 'ECELL_STAFF'), ('PHOTOCIRCLE_STAFF', 'PHOTOCIRCLE_STAFF'), ('SORT_STAFF', 'SORT_STAFF'), ('MUSIC_STAFF', 'MUSIC_STAFF'), ('SPORTS_STAFF', 'SPORTS_STAFF'), ('CULTURAL_STAFF', 'CULTURAL_STAFF')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classs', models.CharField(max_length=30)),
                ('dept', models.CharField(max_length=30)),
                ('email_confirmed', models.BooleanField()),
                ('is_head', models.BooleanField()),
                ('soc_head', models.CharField(choices=[('CSI_HEAD', 'CSI_HEAD'), ('IEEE_HEAD', 'IEEE_HEAD'), ('ISA_HEAD', 'ISA_HEAD'), ('ISTE_HEAD', 'ISTE_HEAD'), ('VESLIT_HEAD', 'VESLIT_HEAD'), ('ECELL_HEAD', 'ECELL_HEAD'), ('PHOTOCIRCLE_HEAD', 'PHOTOCIRCLE_HEAD'), ('SORT_HEAD', 'SORT_HEAD'), ('MUSIC_HEAD', 'MUSIC_HEAD'), ('SPORTS_HEAD', 'SPORTS_HEAD'), ('CULTURAL_HEAD', 'CULTURAL_HEAD')], max_length=30)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.roles')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=30)),
                ('email_confirmed', models.BooleanField()),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.roles')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('membership_required', models.BooleanField(default=0)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 4, 3, 18, 8, 3, 623266, tzinfo=utc))),
                ('event_type', models.CharField(choices=[('HACKATHON', 'HACKATHON'), ('WORKSHOP', 'WORKSHOP'), ('WEBINAR', 'WEBINAR'), ('OTHER', 'OTHER')], max_length=30)),
                ('approved_by', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='APP.staff')),
                ('organizer', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='APP.organizer')),
            ],
        ),
    ]