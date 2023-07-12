# Generated by Django 4.2.2 on 2023-06-26 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=254, verbose_name='текст')),
                ('rate', models.IntegerField(verbose_name='рейтинг')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='кто оставил')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, unique=True, verbose_name='название')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='имя')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='цена')),
                ('datetime_created', models.DateTimeField(verbose_name='дата создания')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_game', to='games.comment', verbose_name='комментарии')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_games', to='games.comment', verbose_name='компания')),
                ('genres', models.ManyToManyField(related_name='games', to='games.genre', verbose_name='жанры')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='имя')),
                ('datetime_created', models.DateTimeField(verbose_name='дата создания')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_company', to='games.comment', verbose_name='комментарии')),
            ],
        ),
    ]
