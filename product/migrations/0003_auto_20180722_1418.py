# Generated by Django 2.0.7 on 2018-07-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20180721_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdynamicdetail',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]