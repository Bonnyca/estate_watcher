# Generated by Django 4.0.4 on 2022-05-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_city', models.CharField(max_length=150)),
                ('address_street', models.CharField(max_length=250)),
                ('date_sold', models.DateTimeField()),
                ('address_state', models.CharField(max_length=3)),
                ('address_zipcode', models.CharField(max_length=5)),
                ('area', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('home_type', models.CharField(max_length=5)),
                ('lot_area', models.IntegerField()),
                ('sold_price', models.IntegerField()),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'houses_coll_test',
            },
        ),
    ]
