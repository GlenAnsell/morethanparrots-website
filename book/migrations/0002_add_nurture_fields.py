# Generated manually for nurture sequence tracking

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscriber',
            name='nurture_day_14_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newslettersubscriber',
            name='nurture_day_2_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newslettersubscriber',
            name='nurture_day_7_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newslettersubscriber',
            name='nurture_unsubscribed',
            field=models.BooleanField(default=False),
        ),
    ]
