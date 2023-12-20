from django.contrib import admin
from .models import unidad, material, tipos_envases, categorias_envases, envase, productor, ingreso

class envase_admin(admin.ModelAdmin):
    list_display = ('id','Categoría','Tipo','Material','Capacidad','Unidad')
    search_fields = ('Categoría',) 

class productor_admin(admin.ModelAdmin):
    list_display = ('id','Razon_Social','Apellido','Nombre')
    ordering = ('Razon_Social',)
    search_fields = ('Razon_Social','Apellido') 
    list_per_page = 30

class ingreso_admin(admin.ModelAdmin):
    list_display = ('id','Envase','Cantidad','Fecha', 'Productor')
    search_fields = ('Envase__Material','Envase__Tipo') 

admin.site.register(unidad)
admin.site.register(material)
admin.site.register(tipos_envases)
admin.site.register(categorias_envases)
admin.site.register(envase,envase_admin)
admin.site.register(productor,productor_admin)
admin.site.register(ingreso,ingreso_admin)