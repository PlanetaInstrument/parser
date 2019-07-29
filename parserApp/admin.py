from django.contrib import admin
from .models import Site, ParserResult, ChangeSite, TemporaryTable

admin.site.register(Site)
# admin.site.register(ParserResult)
admin.site.register(ChangeSite)
admin.site.register(TemporaryTable)

class parserAdmin(admin.ModelAdmin):
    list_filter = ['id_site']
    list_display = ('id_site', 'headline', 'article', 'description', 'price', 'link')

admin.site.register(ParserResult, parserAdmin)
