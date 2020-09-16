# Generated by Django 3.1.1 on 2020-09-16 21:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(default=None, max_length=256, validators=[django.core.validators.MinLengthValidator(2, 'Minimum length should be greater than 2')])),
                ('last_name', models.CharField(default=None, max_length=256, validators=[django.core.validators.MinLengthValidator(2, 'Minimum length should be greater than 2')])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Rather not say', 'Rather not say')], default='Male', max_length=256)),
                ('age', models.PositiveIntegerField(default=18)),
                ('highest_qualification', models.CharField(default='none', max_length=256)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=256, null=True, validators=[django.core.validators.MinLengthValidator(2, 'minimum length should be greater than 2')])),
            ],
            options={
                'db_table': 'sport',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='None', max_length=256, null=True, validators=[django.core.validators.MinLengthValidator(2, 'minimum length should be greater than 2')])),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='UnionTerritory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Union_territory', models.CharField(max_length=256, null=True, validators=[django.core.validators.MinLengthValidator(2, 'minimum length should be greater than 2')])),
            ],
            options={
                'db_table': 'unionterritories',
            },
        ),
        migrations.CreateModel(
            name='user_certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('certificate', models.FileField(upload_to='certificates')),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_Tournament', models.CharField(default='', max_length=256)),
                ('date', models.DateField()),
                ('Venue', models.CharField(max_length=256)),
                ('Event', models.CharField(max_length=256)),
                ('Medal_won', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='sport',
            field=models.ForeignKey(default='Cricket', on_delete=django.db.models.deletion.PROTECT, to='verification.sport'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.ForeignKey(default='Assam', on_delete=django.db.models.deletion.PROTECT, to='verification.state'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
