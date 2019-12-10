# Generated by Django 3.0 on 2019-12-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_feedback', '0003_auto_20191210_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackform',
            name='again',
            field=models.IntegerField(default=3, verbose_name='Would you accept this Trainer again?'),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='discuss',
            field=models.IntegerField(default=2, verbose_name='Did the Trainer allow Sufficient Discussion?'),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='ideas',
            field=models.IntegerField(default=3, verbose_name='Did the Trainer help bring out new group Ideas?'),
        ),
        migrations.AddField(
            model_name='feedbackform',
            name='participate',
            field=models.IntegerField(default=3, verbose_name='Did the Trainer encourage participation?'),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='appropriate',
            field=models.IntegerField(default=3, verbose_name='Was the Course Content appropriate?'),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='clarity',
            field=models.IntegerField(default=3, verbose_name='Was the content fragmented/unclear or clear?'),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='defined',
            field=models.IntegerField(default=3, verbose_name='Were the Objectives well defined?'),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='simplicity',
            field=models.IntegerField(default=3, verbose_name='Was the content simple or complex?'),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='volume',
            field=models.IntegerField(default=3, verbose_name='Was the content not enough or too much?'),
        ),
    ]
