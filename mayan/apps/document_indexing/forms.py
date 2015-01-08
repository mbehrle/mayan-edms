from __future__ import absolute_import

from django import forms

from common.classes import ModelAttribute
from documents.models import Document

from .models import Index, IndexTemplateNode


class IndexForm(forms.ModelForm):
    """
    A standard model form to allow users to create a new index
    """
    class Meta:
        model = Index
        exclude = ('document_types',)


class IndexTemplateNodeForm(forms.ModelForm):
    """
    A standard model form to allow users to create a new index template node
    """
    def __init__(self, *args, **kwargs):
        super(IndexTemplateNodeForm, self).__init__(*args, **kwargs)
        self.fields['index'].widget = forms.widgets.HiddenInput()
        self.fields['parent'].widget = forms.widgets.HiddenInput()
        self.fields['expression'].help_text = ' '.join([unicode(self.fields['expression'].help_text), ModelAttribute.help_text_for(Document, type_names=['indexing'])])

    class Meta:
        model = IndexTemplateNode
