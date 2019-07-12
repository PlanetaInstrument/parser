from django import forms

from .models import Site, ParserResult

class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ('name', 'link', 'link_first', 'atr_products', 'class_products', 'class_value_products', 'atr_category', 'class_category', 'class_value_category',
        'atr_head', 'class_head', 'class_value_head', 'atr_article', 'class_article', 'class_value_article', 'atr_description', 'class_description', 'class_value_description',
        'atr_price', 'class_price', 'class_value_price', 'atr_navigation', 'class_navigation', 'class_value_navigation', 'atr_back', 'class_back', 'class_value_back',
        'atr_link_product', 'class_link_product', 'class_value_link_product')

        # help_texts = {
        #     'name': 'Input name of your site.',
        # }


class ParserResultForm(forms.ModelForm):

    class Meta:
        model = ParserResult
        fields = ('id_site', 'headline', 'article', 'description', 'price', 'link')


class ChooseForm(forms.Form):
    site = forms.ModelChoiceField(queryset=Site.objects.all())

class ViewResultForm(forms.Form):
    view_site = forms.ModelChoiceField(queryset=Site.objects.all())
    view_site_2 = forms.ModelChoiceField(queryset=Site.objects.all())
