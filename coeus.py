


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


class COEUS:


	def __init__(self, api_key, host="http://bioinformatics.ua.pt/coeus"):
		self.__host = host
		self.__key = api

	def triple(self):
		content = requests.get(self.host + 'api/triple/' + sub + '/' + pred + '/' + obj + '/js')
  		return json.loads(content)['results']['bindings']
		
	def query(self,query):
		return sparql.query(self.host, q)
  		
	def write(self,sub, pred, obj):

		if self.key=='':
			raise '[COEUS] undefined API key'
		else:
			content = requests.get(self.host + 'api/' + self.key + '/write/' + sub + '/' + pred + '/' + obj)
			result = json.loads(content)
			if result['status'] != 100:
	  			raise '[COEUS] unable to store triple: ' + result['message']
	  		else:
	  			return true 
	  	
	def update(sub, pred, old_obj, new_obj):
		if self.key == ''
  			raise '[COEUS] undefined API key'
  		else
	  		content = URI.parse(@host + 'api/' + self.key + '/update/' + sub + '/' + pred + '/' + old_obj + ',' + new_obj).read
	  		result = json.loads(content)
	  		if result['status'] != 100:
	  			raise '[COEUS] unable to update triple: ' + result['message']
	  		else:
	  			return true

	def delete(sub, pred, obj):
		if key == ''
  			raise '[COEUS] undefined API key'
  		else
	  		content = requests.get(self.host + 'api/' + self.key + '/delete/' + sub + '/' + pred + '/' + obj)
	  		
	  		result = json.loads(content)
	  		if result['status'] != 100
	  			raise '[COEUS] unable to delete triple: ' + result['message']
	  		else:
	  			return true





