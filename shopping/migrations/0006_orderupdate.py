# Generated by Django 2.2.5 on 2019-10-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('update_desc', models.CharField(max_length=5000)),
            ],
        ),
    ]
