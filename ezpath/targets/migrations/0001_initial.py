# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Specialty'
        db.create_table(u'targets_specialty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('datetime_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children_set', null=True, to=orm['targets.Specialty'])),
        ))
        db.send_create_signal(u'targets', ['Specialty'])

        # Adding model 'University'
        db.create_table(u'targets_university', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('datetime_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('abbreviate', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'targets', ['University'])

        # Adding model 'School'
        db.create_table(u'targets_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('datetime_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('abbreviate', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['targets.University'])),
        ))
        db.send_create_signal(u'targets', ['School'])

        # Adding M2M table for field specialties on 'School'
        m2m_table_name = db.shorten_name(u'targets_school_specialties')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('school', models.ForeignKey(orm[u'targets.school'], null=False)),
            ('specialty', models.ForeignKey(orm[u'targets.specialty'], null=False))
        ))
        db.create_unique(m2m_table_name, ['school_id', 'specialty_id'])


    def backwards(self, orm):
        # Deleting model 'Specialty'
        db.delete_table(u'targets_specialty')

        # Deleting model 'University'
        db.delete_table(u'targets_university')

        # Deleting model 'School'
        db.delete_table(u'targets_school')

        # Removing M2M table for field specialties on 'School'
        db.delete_table(db.shorten_name(u'targets_school_specialties'))


    models = {
        u'targets.school': {
            'Meta': {'object_name': 'School'},
            'abbreviate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'specialties': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['targets.Specialty']", 'symmetrical': 'False'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targets.University']"}),
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