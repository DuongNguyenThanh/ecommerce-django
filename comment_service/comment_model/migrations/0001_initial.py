# Generated by Django 4.1.6 on 2023-03-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=255)),
            ],
        ),
    ]
