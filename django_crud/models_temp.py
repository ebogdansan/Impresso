# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CrudAppMembers(models.Model):
    idmembru = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    cnp = models.IntegerField()
    adresa = models.TextField()

    class Meta:
        managed = False
        db_table = 'crud_app_members'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Membri(models.Model):
    idmembru = models.AutoField(primary_key=True)
    nume = models.CharField(db_column='Nume', max_length=45)  # Field name made lowercase.
    prenume = models.CharField(db_column='Prenume', max_length=45)  # Field name made lowercase.
    cnp = models.CharField(db_column='CNP', max_length=45)  # Field name made lowercase.
    adresa = models.CharField(db_column='Adresa', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membri'


class Membritrupe(models.Model):
    idmembritrupe = models.AutoField(primary_key=True)
    idmembru = models.ForeignKey(Membri, models.DO_NOTHING, db_column='idmembru')
    idtrupa = models.ForeignKey('Trupe', models.DO_NOTHING, db_column='idtrupa')
    rol = models.CharField(db_column='Rol', max_length=45)  # Field name made lowercase.
    datainscriere = models.CharField(db_column='DataInscriere', max_length=45)  # Field name made lowercase.
    activitate = models.CharField(db_column='Activitate', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'membritrupe'


class Trupe(models.Model):
    idtrupa = models.AutoField(primary_key=True)
    numetrupa = models.CharField(db_column='NumeTrupa', max_length=45)  # Field name made lowercase.
    genmuzical = models.CharField(db_column='GenMuzical', max_length=45)  # Field name made lowercase.
    aninfiintare = models.CharField(db_column='AnInfiintare', max_length=45)  # Field name made lowercase.
    tara = models.CharField(db_column='Tara', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trupe'
