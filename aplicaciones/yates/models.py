from django.db import models

# Create your models here.


class pais(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(default=0,max_length=255,blank=False, null=False,unique=True)

    def __str__(self):
         return "Pais: "+str(self.nombre)

    class Meta:

        verbose_name = "Pais"
        verbose_name_plural = "1.Paises"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("iniciarjugada", "IniciarJugada"),
            #("consultarcomprobantes", "ConsultarComprobante"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos


class marca_yates(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(default=0,max_length=255,blank=False, null=False,unique=True)

    def __str__(self):
         return "Marca: "+str(self.nombre)

    class Meta:

        verbose_name = "Marca"
        verbose_name_plural = "2.Marcas"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("iniciarjugada", "IniciarJugada"),
            #("consultarcomprobantes", "ConsultarComprobante"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos

class modelo_yates(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(default=0,max_length=255,blank=False, null=False,unique=True)

    def __str__(self):
         return "Modelos: "+str(self.nombre)

    class Meta:

        verbose_name = "Modelo"
        verbose_name_plural = "3.Modelos"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("iniciarjugada", "IniciarJugada"),
            #("consultarcomprobantes", "ConsultarComprobante"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos

class tipo_combustible_yates(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(default=0,max_length=255,blank=False, null=False,unique=True)

    def __str__(self):
         return "tipo combustible: "+str(self.nombre)

    class Meta:

        verbose_name = "Tipo combustible"
        verbose_name_plural = "4.Tipo de combustible"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("iniciarjugada", "IniciarJugada"),
            #("consultarcomprobantes", "ConsultarComprobante"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos




class yates(models.Model):


    estado = [
        ('disponible','Disponible'),
        ('alquilado','Alquilado'),
        ('comprado','Comprado'),
        ('dañado','Dañado'),
    ]

    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(marca_yates, on_delete=models.CASCADE)
    modelo = models.ForeignKey(modelo_yates, on_delete=models.CASCADE)
    tipo_combustible = models.ForeignKey(tipo_combustible_yates, on_delete=models.CASCADE)
    pais = models.ForeignKey(pais, on_delete=models.CASCADE)
    longitud_del_barco = models.PositiveIntegerField(default=0)
    precio_del_barco = models.FloatField(default=0)

    estado_del_yate = models.CharField("status",
        max_length=150,
        choices=estado,    
        default='disponible'
    )

    nombre = models.CharField(default=0,max_length=11,blank=False, null=False)

    def __str__(self):
         return "Yate: "+str(self.nombre)

    class Meta:

        verbose_name = "Yate"
        verbose_name_plural = "5.Yates"

        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            
            #Permisos para iniciar y consultar jugadas
            #("iniciarjugada", "IniciarJugada"),
            #("consultarcomprobantes", "ConsultarComprobante"),

            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos