# Generated by Django 4.2.4 on 2023-09-01 10:25

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('publish', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prayer.prayer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('text', models.TextField()),
                ('order', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'توضیح دعا'), (2, 'متن دعا'), (3, 'متن قرآن')], default=1)),
                ('prayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prayer.prayer')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('index', models.BooleanField(default=True)),
                ('publish', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prayer.category')),
                ('prayer', models.ManyToManyField(to='prayer.prayer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
