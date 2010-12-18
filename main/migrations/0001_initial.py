# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'Profile'
        db.create_table('main_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('icq', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=30)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('main', ['Profile'])

        # Adding model 'Request'
        db.create_table('main_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Request'])

        # Adding model 'TransactionSignal'
        db.create_table('main_transactionsignal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.TextField')()),
            ('action', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['TransactionSignal'])


    def backwards(self, orm):

        # Deleting model 'Profile'
        db.delete_table('main_profile')

        # Deleting model 'Request'
        db.delete_table('main_request')

        # Deleting model 'TransactionSignal'
        db.delete_table('main_transactionsignal')


    models = {
        'main.profile': {
            'Meta': {'object_name': 'Profile'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'main.request': {
            'Meta': {'object_name': 'Request'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.TextField', [], {})
        },
        'main.transactionsignal': {
            'Meta': {'object_name': 'TransactionSignal'},
            'action': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['main']
