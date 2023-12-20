from django.db import models
   
class unidad(models.Model):
    Unidad = models.CharField(max_length=20, null=False, verbose_name='unidad de medida')
    def __str__(self):
        return self.Unidad
    class Meta:
        db_table = 'unidades'
        verbose_name = 'unidad'
        verbose_name_plural = 'U. de medidas'

class material(models.Model):
    Nombre_Material = models.CharField(max_length=20, null=False, verbose_name='material')
    def __str__(self):
        return self.Nombre_Material
    class Meta:
        db_table = 'materiales'
        verbose_name = 'material'
        verbose_name_plural = 'Materiales'

class tipos_envases(models.Model):
    Nombre = models.CharField(max_length=20, null=False, verbose_name='tipo de envase')
    def __str__(self):
        return self.Nombre
    class Meta:
        db_table = 'tipos_envases'
        verbose_name = 'tipos'
        verbose_name_plural = 'Tipos de envases'

class categorias_envases(models.Model):
    Nombre = models.CharField(max_length=20, null=False, verbose_name='tipo de envase')
    def __str__(self):
        return self.Nombre
    class Meta:
        db_table = 'categorias_envases'
        verbose_name = 'categorias'
        verbose_name_plural = 'Categorias de envases'
    
class envase(models.Model):
    Tipo = models.ForeignKey(tipos_envases, on_delete=models.CASCADE, blank=True, null=True)
    Categoría = models.ForeignKey(categorias_envases, on_delete=models.CASCADE, blank=True, null=True)
    Material = models.ForeignKey(material, on_delete=models.CASCADE, blank=True, null=True)
    Capacidad = models.PositiveIntegerField(default=0)
    Unidad = models.ForeignKey(unidad, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return '%s de %s %d %s (%s)'%(self.Categoría, self.Material, self.Capacidad, self.Unidad, self.Tipo)  
    class Meta:
        db_table = 'envases'
        verbose_name = 'envase'
        verbose_name_plural = 'Envases'
    
class productor(models.Model):
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    Razon_Social=models.CharField(max_length=30,null=True)
    DNI=models.CharField(max_length=30)
    Domicilio=models.CharField(max_length=30)
    Telefono=models.CharField(max_length=30)
    Email=models.EmailField(blank=True, verbose_name='email',null=True)
    def __str__(self) :
          return '%s  %s'%(self.Nombre, self.Apellido)  
    class Meta:
        db_table = 'productores'
        verbose_name = 'productor'
        verbose_name_plural = 'Productores'

class ingreso(models.Model):
    Envase = models.ForeignKey(envase, on_delete=models.CASCADE, blank=True, null=True)
    Cantidad = models.PositiveIntegerField(default=0)
    Productor = models.ForeignKey(productor, on_delete=models.CASCADE, blank=True, null=True)
    Fecha = models.DateField()
    Retirado = models.BooleanField(default='False')
    def __str__(self) :
          return '%s  %s'%(self.Envase, self.Cantidad)  
    class Meta:
        db_table = 'ingresos'
        verbose_name = 'ingreso'
        verbose_name_plural = 'Ingresos'