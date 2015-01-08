from __future__ import absolute_import

from rest_framework import serializers

from .models import DocumentCheckout


class DocumentCheckoutSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Hide this import otherwise strange circular import error occur
        from documents.serializers import DocumentSerializer

        super(DocumentCheckoutSerializer, self).__init__(*args, **kwargs)
        self.fields['document'] = DocumentSerializer()

    class Meta:
        model = DocumentCheckout
        read_only_fields = ('user_content_type', 'user_object_id')


class NewDocumentCheckoutSerializer(serializers.Serializer):
    document = serializers.IntegerField()
    expiration_datetime = serializers.DateTimeField()
    block_new_version = serializers.BooleanField()
