# Generated by Django 4.1.4 on 2023-01-08 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trouvailleapi', '0012_alter_tripexperience_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripexperience',
            name='note',
            field=models.CharField(default='', max_length=150),
        ),
    ]
