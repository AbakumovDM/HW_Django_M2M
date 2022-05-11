# Generated by Django 3.1.2 on 2022-05-09 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20220509_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlechapter',
            options={'verbose_name': 'Раздел статьи', 'verbose_name_plural': 'Разделы статьи'},
        ),
        migrations.AddField(
            model_name='articlechapter',
            name='basechapter',
            field=models.BooleanField(default=False, verbose_name='основной'),
        ),
    ]