# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IMAPEmail'
        db.create_table(u'sources_imapemail', (
            (u'emailbasemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sources.EmailBaseModel'], unique=True, primary_key=True)),
            ('mailbox', self.gf('django.db.models.fields.CharField')(default='INBOX', max_length=64)),
        ))
        db.send_create_signal(u'sources', ['IMAPEmail'])

        # Adding model 'IntervalBaseModel'
        db.create_table(u'sources_intervalbasemodel', (
            (u'outofprocesssource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sources.OutOfProcessSource'], unique=True, primary_key=True)),
            ('interval', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
            ('document_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['documents.DocumentType'], null=True, blank=True)),
            ('uncompress', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'sources', ['IntervalBaseModel'])

        # Adding model 'POP3Email'
        db.create_table(u'sources_pop3email', (
            (u'emailbasemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sources.EmailBaseModel'], unique=True, primary_key=True)),
            ('timeout', self.gf('django.db.models.fields.PositiveIntegerField')(default=60)),
        ))
        db.send_create_signal(u'sources', ['POP3Email'])

        # Adding model 'EmailBaseModel'
        db.create_table(u'sources_emailbasemodel', (
            (u'intervalbasemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sources.IntervalBaseModel'], unique=True, primary_key=True)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('ssl', self.gf('django.db.models.fields.BooleanField')()),
            ('port', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=96)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=96)),
        ))
        db.send_create_signal(u'sources', ['EmailBaseModel'])

    def backwards(self, orm):
        # Deleting model 'IMAPEmail'
        db.delete_table(u'sources_imapemail')

        # Deleting model 'IntervalBaseModel'
        db.delete_table(u'sources_intervalbasemodel')

        # Deleting model 'POP3Email'
        db.delete_table(u'sources_pop3email')

        # Deleting model 'EmailBaseModel'
        db.delete_table(u'sources_emailbasemodel')

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'documents.documenttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'DocumentType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'sources.emailbasemodel': {
            'Meta': {'ordering': "('title',)", 'object_name': 'EmailBaseModel', '_ormbases': [u'sources.IntervalBaseModel']},
            'host': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'intervalbasemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.IntervalBaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '96'}),
            'port': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ssl': ('django.db.models.fields.BooleanField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '96'})
        },
        u'sources.imapemail': {
            'Meta': {'ordering': "('title',)", 'object_name': 'IMAPEmail', '_ormbases': [u'sources.EmailBaseModel']},
            u'emailbasemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.EmailBaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'mailbox': ('django.db.models.fields.CharField', [], {'default': "'INBOX'", 'max_length': '64'})
        },
        u'sources.interactivesource': {
            'Meta': {'ordering': "('title',)", 'object_name': 'InteractiveSource', '_ormbases': [u'sources.Source']},
            u'source_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.Source']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sources.intervalbasemodel': {
            'Meta': {'ordering': "('title',)", 'object_name': 'IntervalBaseModel', '_ormbases': [u'sources.OutOfProcessSource']},
            'document_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['documents.DocumentType']", 'null': 'True', 'blank': 'True'}),
            'interval': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            u'outofprocesssource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.OutOfProcessSource']", 'unique': 'True', 'primary_key': 'True'}),
            'uncompress': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'sources.outofprocesssource': {
            'Meta': {'ordering': "('title',)", 'object_name': 'OutOfProcessSource', '_ormbases': [u'sources.Source']},
            u'source_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.Source']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sources.pop3email': {
            'Meta': {'ordering': "('title',)", 'object_name': 'POP3Email', '_ormbases': [u'sources.EmailBaseModel']},
            u'emailbasemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.EmailBaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'timeout': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'})
        },
        u'sources.source': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Source'},
            'blacklist': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'whitelist': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'sources.sourcetransformation': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SourceTransformation'},
            'arguments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'transformation': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'sources.stagingfoldersource': {
            'Meta': {'ordering': "('title',)", 'object_name': 'StagingFolderSource', '_ormbases': [u'sources.InteractiveSource']},
            'delete_after_upload': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'folder_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'interactivesource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.InteractiveSource']", 'unique': 'True', 'primary_key': 'True'}),
            'preview_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'preview_width': ('django.db.models.fields.IntegerField', [], {}),
            'uncompress': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'sources.watchfoldersource': {
            'Meta': {'ordering': "('title',)", 'object_name': 'WatchFolderSource', '_ormbases': [u'sources.OutOfProcessSource']},
            'delete_after_upload': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'folder_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'interval': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'outofprocesssource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.OutOfProcessSource']", 'unique': 'True', 'primary_key': 'True'}),
            'uncompress': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'sources.webformsource': {
            'Meta': {'ordering': "('title',)", 'object_name': 'WebFormSource', '_ormbases': [u'sources.InteractiveSource']},
            u'interactivesource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sources.InteractiveSource']", 'unique': 'True', 'primary_key': 'True'}),
            'uncompress': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['sources']
