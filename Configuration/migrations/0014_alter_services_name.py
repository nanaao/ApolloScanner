# Generated by Django 4.0.1 on 2022-03-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0013_serviceslog_method_serviceslog_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(choices=[('1', 'HTTP服务')], max_length=2, unique=True, verbose_name='配置名称'),
        ),
    ]
