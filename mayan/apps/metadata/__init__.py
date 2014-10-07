from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from acls.api import class_permissions
from common.utils import encapsulate
from documents.models import Document, DocumentType
from navigation.api import (register_links, register_multi_item_links,
    register_sidebar_template, register_model_list_columns)
from project_setup.api import register_setup
from rest_api.classes import APIEndPoint

from .api import get_metadata_string
from .links import (metadata_edit, metadata_view, metadata_multiple_edit,
    metadata_add, metadata_multiple_add, metadata_remove, metadata_multiple_remove,
    setup_metadata_type_list, setup_metadata_type_edit, setup_metadata_type_delete,
    setup_metadata_type_create, setup_metadata_set_list, setup_metadata_set_edit,
    setup_metadata_set_members, setup_metadata_set_delete, setup_metadata_set_create,
    setup_document_type_metadata)
from .models import MetadataSet, MetadataType
from .permissions import (PERMISSION_METADATA_DOCUMENT_ADD,
                          PERMISSION_METADATA_DOCUMENT_EDIT,
                          PERMISSION_METADATA_DOCUMENT_REMOVE,
                          PERMISSION_METADATA_DOCUMENT_VIEW)
from .urls import api_urls

register_links(['metadata:metadata_add', 'metadata:metadata_edit', 'metadata:metadata_remove', 'metadata:metadata_view'], [metadata_add, metadata_edit, metadata_remove], menu_name='sidebar')
register_links(Document, [metadata_view], menu_name='form_header')
register_multi_item_links(['documents:document_find_duplicates', 'folders:folder_view', 'indexes:index_instance_node_view', 'documents:document_type_document_list', 'search:search', 'search:results', 'linking:document_group_view', 'documents:document_list', 'documents:document_list_recent', 'tags:tag_tagged_item_list'], [metadata_multiple_add, metadata_multiple_edit, metadata_multiple_remove])

register_links(MetadataType, [setup_metadata_type_edit, setup_metadata_type_delete])
register_links([MetadataType, 'metadata:setup_metadata_type_list', 'metadata:setup_metadata_type_create'], [setup_metadata_type_list, setup_metadata_type_create], menu_name='secondary_menu')

register_links(MetadataSet, [setup_metadata_set_edit, setup_metadata_set_members, setup_metadata_set_delete])
register_links([MetadataSet, 'metadata:setup_metadata_set_list', 'metadata:setup_metadata_set_create'], [setup_metadata_set_list, setup_metadata_set_create], menu_name='secondary_menu')

register_links(DocumentType, [setup_document_type_metadata])

register_sidebar_template(['metadata:setup_metadata_type_list'], 'metadata_type_help.html')
register_sidebar_template(['metadata:setup_metadata_set_list'], 'metadata_set_help.html')

register_setup(setup_metadata_set_list)
register_setup(setup_metadata_type_list)

class_permissions(Document, [
    PERMISSION_METADATA_DOCUMENT_ADD, PERMISSION_METADATA_DOCUMENT_EDIT,
    PERMISSION_METADATA_DOCUMENT_REMOVE, PERMISSION_METADATA_DOCUMENT_VIEW,
])

register_model_list_columns(Document, [
        {
            'name': _(u'Metadata'), 'attribute': encapsulate(lambda x: get_metadata_string(x))
        },
    ])

endpoint = APIEndPoint('metadata')
endpoint.register_urls(api_urls)
endpoint.add_endpoint('metadatatype-list', _(u'Returns a list of all the metadata types.'))
