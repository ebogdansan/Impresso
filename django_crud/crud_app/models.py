from django.db import models

# Create your models here.
class Membru(models.Model):
    idmembru= models.AutoField(primary_key=True)
    nume= models.CharField(db_column='Nume',max_length=100)
    prenume = models.CharField(db_column='Prenume',max_length=100)
    cnp= models.CharField(db_column='CNP',max_length=13)
    adresa = models.CharField(db_column='Adresa',max_length=255)

    class Meta:  #se foloseste atunci cand ai deja o bd creata in serverul comun, e ca un manual de instructiuni pt django
        db_table = 'membri'
        verbose_name = 'Membru'
        verbose_name_plural = 'Membri'
    
    def __str__(self):
        return f"{self.nume} {self.prenume}"
    
class Trupa(models.Model):
    idtrupa = models.AutoField(primary_key=True)
    numetrupa = models.CharField(db_column='NumeTrupa',max_length=100)
    genmuzical = models.CharField(db_column='GenMuzical',max_length=50)
    aninfiintare = models.CharField(db_column='AnInfiintare',max_length=4)
    tara = models.CharField(db_column='Tara',max_length=50)

    class Meta:
        db_table = 'trupe'
        verbose_name = 'Trupa'
        verbose_name_plural = 'Trupe'

    def __str__(self):
        return self.numetrupa
    
class MembruTrupa(models.Model):
    idmembritrupe= models.AutoField(primary_key=True)
    membru= models.ForeignKey(Membru, on_delete=models.CASCADE, db_column='idmembru')
    trupa= models.ForeignKey(Trupa, on_delete=models.CASCADE, db_column='idtrupa')
    rol= models.CharField(db_column='Rol',max_length=50)
    datainscriere= models.CharField(db_column='DataInscriere',max_length=12)
    activitate= models.CharField(db_column='Activitate',max_length=20)

    class Meta:
        db_table = 'membritrupe'
        verbose_name = 'Membru Trupa'
        verbose_name_plural = 'Membri Trupe'
        unique_together = ['membru', 'trupa']
    
    def __str__(self):
        return f"{self.membru} - {self.trupa} - ({self.rol})"
    