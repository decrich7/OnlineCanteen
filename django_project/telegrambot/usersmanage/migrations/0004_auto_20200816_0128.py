# Generated by Django 2.2.3 on 2020-08-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersmanage', '0003_auto_20200816_0047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Покупка', 'verbose_name_plural': 'Покупки'},
        ),
        migrations.AlterModelOptions(
            name='referral',
            options={'verbose_name': 'Реферал', 'verbose_name_plural': 'Рефералы'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость'),
        ),
    ]