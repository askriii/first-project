from django.db import models
class Bd(models.Model):
    PRODESSION = (
        ('P', 'Professeur'),
        ('E', 'Etudiant'),
    )
    CIN	=models.CharField(max_length=20)
    Nom=models.CharField(max_length=20)
    Prenom=models.CharField(max_length=20)
    Adresse=models.CharField(max_length=20)
    Email=models.EmailField()
    Numerotelephone=models.PositiveIntegerField()
    Profession=models.CharField(max_length=1, choices=PRODESSION, default='E')
    Departement=models.CharField(max_length=20)

    def __str__(self):
        return "%s %s" % (self.Nom, self.Prenom)

# Create your models here.



# Create your models here.
