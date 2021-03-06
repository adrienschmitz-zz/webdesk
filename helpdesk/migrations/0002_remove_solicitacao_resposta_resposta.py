# Generated by Django 4.0.2 on 2022-03-27 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacao',
            name='resposta',
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.TextField(verbose_name='Resposta')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('solicitacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.solicitacao')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
