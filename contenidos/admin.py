from django.contrib import admin
from contenidos.models import Diapositiva, Novedad, Pagina, Album, TipoDiapositiva, Idioma
from file_resubmit.admin import AdminResubmitImageWidget, AdminResubmitFileWidget, AdminResubmitMixin

from imagekit.admin import AdminThumbnail

# Register your models here.


@admin.register(Diapositiva)
class DiapositivaAdmin(AdminResubmitMixin, admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='imagen_miniatura')
    list_display = ('titulo', 'slug', 'importancia', 'tipo_diapositiva', 'idioma', 'admin_thumbnail')
    list_filter = ['idioma']
    list_editable = ['importancia']

# admin.site.register(Diapositiva, DiapositivaAdmin)
admin.site.register(Novedad)
admin.site.register(Pagina)
admin.site.register(Album)
# admin.site.register(TipoDiapositiva)
# admin.site.register(Idioma)

