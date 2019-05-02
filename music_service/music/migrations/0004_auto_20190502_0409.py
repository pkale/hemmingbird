# Generated by Django 2.2.1 on 2019-05-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190502_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tailors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('location', models.CharField(choices=[('V', 'Vietnam'), ('T', 'Thailand'), ('S', 'Singapore')], default='', max_length=1)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='shoulder_length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customers',
            name='sleeve_length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customers',
            name='waist_length',
            field=models.IntegerField(default=0),
        ),
    ]