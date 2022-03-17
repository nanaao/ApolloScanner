# Generated by Django 4.0.1 on 2022-03-08 15:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Assets', '0002_alter_assetlist_cname_alter_assetlist_middle_ware_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExploitRegister',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='序号')),
                ('exploit_name', models.CharField(db_column='exploit_name', max_length=32, verbose_name='负载名称')),
                ('vulnerable_id', models.CharField(blank=True, db_column='vulnerable_id', max_length=32, null=True, verbose_name='漏洞编号')),
                ('category', models.CharField(choices=[('1', 'WEB漏洞'), ('2', '系统漏洞')], max_length=2, verbose_name='漏洞类型')),
                ('file_object', models.FileField(null=True, upload_to='VulnerableScan/ExploitFiles/', verbose_name='负载上传')),
                ('description', models.TextField(db_column='description', verbose_name='漏洞描述')),
                ('timestamp', models.DateField(db_column='timestamp', verbose_name='创建日期')),
            ],
            options={
                'verbose_name': '负载管理',
                'verbose_name_plural': '负载管理',
            },
        ),
        migrations.CreateModel(
            name='VulnerableScanResult',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='序号')),
                ('task_id', models.IntegerField(db_column='task_id', verbose_name='对应工单序号')),
                ('task_name', models.CharField(db_column='task_name', max_length=32, verbose_name='工单名称')),
                ('vulnerable_id', models.CharField(db_column='vulnerable_id', max_length=32, verbose_name='漏洞编号')),
                ('ip_address', models.GenericIPAddressField(db_column='ip_address', verbose_name='目标地址')),
                ('port', models.IntegerField(db_column='port', null=True, verbose_name='目标端口')),
                ('description', models.TextField(db_column='description', verbose_name='任务过程描述')),
                ('result_flag', models.BooleanField(db_column='result_flag', verbose_name='测试结果')),
                ('timestamp', models.DateField(db_column='timestamp', verbose_name='结束日期')),
            ],
            options={
                'verbose_name': '扫描结果',
                'verbose_name_plural': '扫描结果',
            },
        ),
        migrations.CreateModel(
            name='VulnerableScanTasks',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(db_column='name', max_length=32, verbose_name='任务名称')),
                ('timestamp', models.DateField(db_column='timestamp', default=django.utils.timezone.now, verbose_name='创建日期')),
                ('exploit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='VulnerableScan.exploitregister', verbose_name='漏洞负载选择')),
                ('target', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Assets.assetlist', verbose_name='目标选择')),
            ],
            options={
                'verbose_name': '任务项',
                'verbose_name_plural': '任务项',
            },
        ),
    ]
