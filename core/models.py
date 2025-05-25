from django.db import models

class Grupo(models.Model):
    grado = models.CharField(max_length=20)
    nombre = models.CharField(max_length=10)
    jornada = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.grado} - {self.nombre} ({self.jornada})"

class Area(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.TextField()
    nombre_padre = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Docente(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    grupos = models.ManyToManyField(Grupo)

    def __str__(self):
        return self.nombres

class Calificacion(models.Model):
    PRIMER_PERIODO = 'PRIMERO'
    SEGUNDO_PERIODO = 'SEGUNDO'
    TERCER_PERIODO = 'TERCERO'
    FINAL_PERIODO = 'FINAL'
    PERIODOS = [
        (PRIMER_PERIODO, 'Primero'),
        (SEGUNDO_PERIODO, 'Segundo'),
        (TERCER_PERIODO, 'Tercero'),
        (FINAL_PERIODO, 'Final'),
    ]

    estudiante   = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    area         = models.ForeignKey(Area, on_delete=models.CASCADE)
    periodo      = models.CharField(max_length=8, choices=PERIODOS)
    nota         = models.FloatField()
    observaciones= models.TextField(blank=True)
    faltas       = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.estudiante} – {self.area} – {self.get_periodo_display()}"