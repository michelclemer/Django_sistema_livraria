# Generated by Django 3.2.8 on 2022-02-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaLivraria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='titulo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='livro',
            name='description',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='image',
            field=models.ImageField(null=True, upload_to='imagens/', verbose_name='Image'),
        ),
    ]
