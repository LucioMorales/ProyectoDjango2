# Generated by Django 2.2 on 2020-07-01 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=243)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5)),
                ('calle', models.CharField(max_length=20)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('descuento', models.IntegerField()),
                ('monto_final', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('web', models.CharField(max_length=150)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Categoria')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Venta')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comercio.Direccion'),
        ),
    ]
