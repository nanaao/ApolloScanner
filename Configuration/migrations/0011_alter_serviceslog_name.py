# Generated by Django 4.0.1 on 2022-03-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuration', '0010_alter_services_name_alter_serviceslog_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceslog',
            name='name',
            field=models.CharField(choices=[('1', 'HTTP日志')], default='1', editable=False, max_length=2, unique=True, verbose_name='配置名称'),
        ),
    ]
