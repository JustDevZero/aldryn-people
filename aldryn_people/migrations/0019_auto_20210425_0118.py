# Generated by Django 2.1.15 on 2021-04-25 01:18

from django.db import migrations
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_people', '0018_auto_20160802_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouptranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='aldryn_people.Group'),
        ),
        migrations.AlterField(
            model_name='persontranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='aldryn_people.Person'),
        ),
    ]
