from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistories', '0002_alter_medicalhistory_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalhistory',
            old_name='notes',
            new_name='patient_name',
        ),
    ]
