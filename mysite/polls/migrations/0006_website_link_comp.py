# Generated by Django 4.2.3 on 2023-09-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0005_website_groups_link_website_parsed_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="website",
            name="link_comp",
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
