# Generated by Django 2.0.7 on 2018-08-24 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180823_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kind', models.CharField(choices=[('E', 'Email'), ('p', 'Telefone')], max_length=1)),
                ('value', models.CharField(max_length=255)),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Speaker')),
            ],
        ),
    ]