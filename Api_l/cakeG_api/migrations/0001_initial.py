# Generated by Django 4.0.3 on 2022-03-20 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'occation',
                'verbose_name_plural': 'occations',
            },
        ),
        migrations.CreateModel(
            name='All_cakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='./media')),
                ('price', models.IntegerField()),
                ('occation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeG_api.occation')),
            ],
        ),
    ]
