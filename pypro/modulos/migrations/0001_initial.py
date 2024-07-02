from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('titulo', models.CharField(max_length=64)),
                ('publico', models.TextField(null=True)),
                ('descricao', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
