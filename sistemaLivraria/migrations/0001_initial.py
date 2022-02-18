# Generated by Django 3.2.8 on 2022-02-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='imagens/', verbose_name='Imagem')),
                ('description', models.TextField(null=True, verbose_name='Descrição')),
            ],
        ),
    ]