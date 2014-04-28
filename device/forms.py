from django.forms import ModelForm
from device.models import SearchHistory


class SearchHistoryForm(ModelForm):
    class Meta:
        model = SearchHistory
