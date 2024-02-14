# Generated by Django 4.2.10 on 2024-02-14 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extent', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('website_url', models.CharField(max_length=100)),
                ('image', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=250)),
                ('profile_img', models.CharField(max_length=100)),
                ('cover_img', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=250)),
                ('cover_img', models.CharField(default='', max_length=100)),
                ('is_draft', models.BooleanField(default=True)),
                ('is_upcoming', models.BooleanField(default=False)),
                ('is_private', models.BooleanField(default=False)),
                ('modified_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TripExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='', max_length=150)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_trip_experiences', to='trouvailleapi.experience')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_trip_experiences', to='trouvailleapi.trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trouvailleapi.destination')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trouvailleapi.trip')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='destinations',
            field=models.ManyToManyField(related_name='destination_trips', through='trouvailleapi.TripDestination', to='trouvailleapi.destination'),
        ),
        migrations.AddField(
            model_name='trip',
            name='duration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='duration_trips', to='trouvailleapi.duration'),
        ),
        migrations.AddField(
            model_name='trip',
            name='experiences',
            field=models.ManyToManyField(related_name='experience_trips', through='trouvailleapi.TripExperience', to='trouvailleapi.experience'),
        ),
        migrations.AddField(
            model_name='trip',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_trips', to='trouvailleapi.season'),
        ),
        migrations.AddField(
            model_name='trip',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='styled_trips', to='trouvailleapi.style'),
        ),
        migrations.AddField(
            model_name='trip',
            name='traveler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveled_trips', to='trouvailleapi.traveler'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_subscriptions', to='trouvailleapi.traveler')),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveler_subscriptions', to='trouvailleapi.traveler')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_images', to='trouvailleapi.trip')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_trips', to='trouvailleapi.traveler')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_favorited', to='trouvailleapi.trip')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='experience_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='trouvailleapi.experiencetype'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=150)),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveler_comments', to='trouvailleapi.traveler')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_comments', to='trouvailleapi.trip')),
            ],
        ),
    ]
