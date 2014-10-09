from django.contrib import admin
from contenidos.models import Diapositiva, Novedad, Pagina, Album, TipoDiapositiva, Idioma, Foto
from file_resubmit.admin import AdminResubmitImageWidget, AdminResubmitFileWidget, AdminResubmitMixin

from imagekit.admin import AdminThumbnail

# Register your models here.


@admin.register(Diapositiva)
class DiapositivaAdmin(AdminResubmitMixin, admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='imagen_miniatura')
    list_display = ('titulo', 'slug', 'importancia', 'tipo_diapositiva', 'idioma', 'admin_thumbnail')
    list_filter = ['idioma']
    list_editable = ['importancia']


@admin.register(Novedad)
class NovedadAdmin(AdminResubmitMixin, admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='imagen_miniatura')
    list_display = ('titulo', 'slug', 'idioma', 'pub_date', 'admin_thumbnail')
    list_filter = ['idioma']

@admin.register(Pagina)
class PaginaAdmin(AdminResubmitMixin, admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'idioma', 'url')
    list_filter = ['idioma']

    def url(self, obj):
        return '/contenidos/pagina/%s/' % obj.slug 

class FotoInline(admin.TabularInline):
    model = Foto

@admin.register(Album)
class AlbumAdmin(AdminResubmitMixin, admin.ModelAdmin):
    #admin_thumbnail = AdminThumbnail(image_field='imagen_miniatura')
    list_display = ('titulo', 'slug', 'idioma')
    list_filter = ['idioma']
    date_hierarchy = 'pub_date'
    inlines = [FotoInline, ]



# admin.site.register(Diapositiva, DiapositivaAdmin)
# admin.site.register(Novedad)
# admin.site.register(Pagina)
# admin.site.register(Album)
admin.site.register(TipoDiapositiva)
admin.site.register(Idioma)

