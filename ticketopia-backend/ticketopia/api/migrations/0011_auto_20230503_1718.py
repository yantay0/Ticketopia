# Generated by Django 3.2 on 2023-05-03 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_eventlocation_end_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='tickets',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='event_location',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
        migrations.AddField(
            model_name='ticket',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='api.account'),
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('dance_floor', 'Dance Floor'), ('vip', 'VIP'), ('seating', 'Seating Area')], max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('event_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.eventlocation')),
            ],
            options={
                'unique_together': {('name', 'event_location')},
            },
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tickettype'),
        ),
    ]