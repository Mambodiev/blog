# Generated by Django 3.2 on 2021-09-11 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_privacy_policy_terms_of_use'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Privacy_policy',
            new_name='PrivacyPolicy',
        ),
        migrations.RenameModel(
            old_name='Terms_of_use',
            new_name='TermsOfUse',
        ),
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'verbose_name_plural': 'Privacy_policies'},
        ),
    ]
