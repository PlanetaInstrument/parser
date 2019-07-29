from .models import ParserResult
import django_filters

class ParserResultFilter(django_filters.FilterSet):
    class Meta:
        model = ParserResult
        fields = ['article']
