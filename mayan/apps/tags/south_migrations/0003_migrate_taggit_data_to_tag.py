# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.db.utils import OperationalError, ProgrammingError


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        try:
            db.start_transaction()
            sql1 = 'INSERT INTO tags_tag (id, label, color) ' \
                'SELECT tt.id, tt.name, tp.color ' \
                'FROM taggit_tag AS tt ' \
                'INNER JOIN tags_tagproperties AS tp ON tt.id = tp.tag_id;'
            sql2 = 'INSERT INTO tags_tag_document (tag_id, document_id) ' \
                'SELECT tti.tag_id, tti.object_id FROM taggit_taggeditem AS tti;'
            db.execute(sql1)
            db.execute(sql2)
        except (OperationalError, ProgrammingError):
            db.rollback_transaction()
        else:
            db.commit_transaction()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'documents.document': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Document'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'document_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'documents'", 'null': 'True', 'to': u"orm['documents.DocumentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '48', 'blank': 'True'})
        },
        u'documents.documenttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'DocumentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'document': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['documents.Document']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'})
        },
        u'tags.tagproperties': {
            'Meta': {'object_name': 'TagProperties'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': u"orm['tags.Tag']"})
        }
    }

    complete_apps = ['tags']
    symmetrical = True
