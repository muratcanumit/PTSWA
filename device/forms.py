from django import forms
from django.utils.translation import ugettext as _


class SearchForm(forms.Form):
    survelliance_key = forms.CharField(required=True,
                                       label=_('Survelliance Key'),
                                       error_messages={
                                       'required': _("Enter Valid Key")})
