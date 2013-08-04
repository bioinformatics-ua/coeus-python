# -*- coding: utf-8 -*-


__title__ = 'coeus'
__version__ = '0.1-dev'
__author__ = 'Luís A. Bastião Silva'
__license__ = 'CC-BY-NC'
__copyright__ = 'Copyright 2013, Luís Bastião Silva, Universidade de Aveiro'
__url__ = 'http://bioinformatics.ua.pt/coeus'

__maintainer__ = 'Luís A. Bastião Silva'
__email__ = 'bastiao@ua.pt'

import sys
import time
import json
import requests
import sparql


class COEUS(object):


	def __init__(self, api_key, host="http://bioinformatics.ua.pt/coeus/"):
		self.host = host
		self.key = api_key

	def triple(self, sub, pred, obj):
		content = requests.get(self.host + 'api/triple/' + sub + '/' + pred + '/' + obj + '/js')
		print self.host + 'api/triple/' + sub + '/' + pred + '/' + obj + '/js'
		print content.text
		print content.json()
  		return json.loads(content)#['results']['bindings']
		
	def query(self,query):
		return sparql.query(self.host, query)
  		
	def write(self,sub, pred, obj):

		if self.key=='':
			raise '[COEUS] undefined API key'
		else:
			content = requests.get(self.host + 'api/' + self.key + '/write/' + sub + '/' + pred + '/' + obj)
			result = json.loads(content)
			if content.status_code != 100:
	  			raise '[COEUS] unable to store triple: ' + result['message']
	  		else:
	  			return true 
	  	
	def update(self, sub, pred, old_obj, new_obj):
		if self.key == '':
  			raise '[COEUS] undefined API key'
  		else:
	  		content = requests.get(self.host + 'api/' + self.key + '/update/' + sub + '/' + pred + '/' + old_obj + ',' + new_obj).read
	  		result = json.loads(content)
	  		if content.status_code != 100:
	  			raise '[COEUS] unable to update triple: ' + result['message']
	  		else:
	  			return true

	def delete(self,sub, pred, obj):
		if self.key == '':
  			raise '[COEUS] undefined API key'
  		else:
	  		content = requests.get(self.host + 'api/' + self.key + '/delete/' + sub + '/' + pred + '/' + obj)
	  		
	  		result = json.loads(content)
	  		if content.status_code != 100:
	  			raise '[COEUS] unable to delete triple: ' + result['message']
	  		else:
	  			return true





