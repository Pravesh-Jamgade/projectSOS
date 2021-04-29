# Generated by Django 2.2.6 on 2021-04-28 11:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntityModel',
            fields=[
                ('entity_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entity_name', models.CharField(max_length=50)),
                ('CHOICES', models.CharField(choices=[('HL', 'Hospital'), ('PN', 'Person'), ('AE', 'Active'), ('IE', 'Inactive')], default='PN', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ToolsModels',
            fields=[
                ('tool_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tool_name', models.CharField(max_length=100)),
                ('tool_qty', models.IntegerField()),
                ('tool_state', models.CharField(choices=[('HL', 'Hospital'), ('PN', 'Person'), ('AE', 'Active'), ('IE', 'Inactive')], default='IE', max_length=3)),
                ('tool_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='help_api.EntityModel')),
            ],
        ),
        migrations.CreateModel(
            name='SOSModel',
            fields=[
                ('sos_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sos_description', models.TextField()),
                ('sos_date', models.DateTimeField(auto_now=True)),
                ('sos_state', models.CharField(choices=[('HL', 'Hospital'), ('PN', 'Person'), ('AE', 'Active'), ('IE', 'Inactive')], default='IE', max_length=3)),
                ('sos_tag', models.CharField(choices=[('BD', 'Bed'), ('ONRL', 'Oxygen Refill'), ('EYCR', 'Empty Cylinder'), ('FLCR', 'Full Cylinder'), ('NL', 'NULL')], default='NL', max_length=4)),
                ('sos_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='help_api.EntityModel')),
            ],
        ),
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lane', models.CharField(db_index=True, editable=False, max_length=250, verbose_name='lane')),
                ('town', models.CharField(db_index=True, editable=False, max_length=300, verbose_name='town')),
                ('district', models.CharField(db_index=True, editable=False, max_length=300, verbose_name='district')),
                ('state', models.CharField(db_index=True, editable=False, max_length=300, verbose_name='state')),
                ('contact_phone', models.CharField(editable=False, max_length=10)),
                ('contact_alternate_phone', models.CharField(editable=False, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_api.EntityModel')),
            ],
        ),
    ]
