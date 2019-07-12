from django.contrib import admin
from .models import Site, ParserResult, ChangeSite, TemporaryTable

admin.site.register(Site)
admin.site.register(ParserResult)
admin.site.register(ChangeSite)
admin.site.register(TemporaryTable)
