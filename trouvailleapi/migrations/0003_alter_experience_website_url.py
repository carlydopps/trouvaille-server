# Generated by Django 4.2.10 on 2024-02-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trouvailleapi', '0002_alter_experience_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='website_url',
            field=models.CharField(max_length=250),
        ),
    ]
