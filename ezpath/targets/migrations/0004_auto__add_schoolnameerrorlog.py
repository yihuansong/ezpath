# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SchoolNameErrorLog'
        db.create_table(u'targets_schoolnameerrorlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('datetime_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('university_name', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'targets', ['SchoolNameErrorLog'])


    def backwards(self, orm):
        # Deleting model 'SchoolNameErrorLog'
        db.delete_table(u'targets_schoolnameerrorlog')


    models = {
        u'targets.area': {
            'Meta': {'object_name': 'Area'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'})
        },
        u'targets.school': {
            'Meta': {'object_name': 'School'},
            'abbreviate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targets.Area']"}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'specialties': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targets.Specialty']", 'symmetrical': 'False'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targets.University']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'targets.schoolnameerrorlog': {
            'Meta': {'object_name': 'SchoolNameErrorLog'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'university_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'targets.specialty': {
            'Meta': {'object_name': 'Specialty'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children_set'", 'null': 'True', 'to': u"orm['targets.Specialty']"})
        },
        u'targets.university': {
            'Meta': {'object_name': 'University'},
            'abbreviate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['targets']