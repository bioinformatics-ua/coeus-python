# -*- coding: utf-8 -*-

# Copyright 2013, Luís Bastião Silva, Universidade de Aveiro
# Authors: Luis A. Bastiao Silva <luis.kop@gmail.com> 

__title__ = 'coeus'
__version__ = '0.1-dev'
__author__ = 'Luís A. Bastião Silva'
__license__ = 'CC-BY-NC'
__copyright__ = 'Copyright 2013, Luís Bastião Silva, Universidade de Aveiro'
__url__ = 'http://bioinformatics.ua.pt/coeus'

__maintainer__ = 'Luís A. Bastião Silva'
__email__ = 'bastiao@ua.pt'
__version__ = '0.1-dev'


import sys
import time
import json
import requests
from SPARQLWrapper import SPARQLWrapper, JSON

class COEUS(object):


	def __init__(self, api_key, host="http://bioinformatics.ua.pt/coeus/"):
		self.host = host
		self.key = api_key

	def triple(self, sub, pred, obj):
		content = requests.get(self.host + 'api/triple/' + sub + '/' + pred + '/' + obj + '/js')
		print self.host + 'api/triple/' + sub + '/' + pred + '/' + obj + '/js'
  		return json.loads(content.text)['results']['bindings']
		
	def query(self,query):




		sparql = SPARQLWrapper(self.host+"sparql")
		sparql.setQuery(query)
  		sparql.setReturnFormat(JSON)
  		results = sparql.query()
  		return results.convert()
  		

	def write(self,sub, pred, obj):

		if self.key=='':
			raise '[COEUS] undefined API key'
		else:
			content = requests.get(self.host + 'api/' + self.key + '/write/' + sub + '/' + pred + '/' + obj)
			result = json.loads(content.text)

			if result['status'] != 100:
	  			raise Exception('[COEUS] unable to store triple ')
	  		else:
	  			return True 
	  	
	def update(self, sub, pred, old_obj, new_obj):
		if self.key == '':
  			raise '[COEUS] undefined API key'
  		else:
	  		content = requests.get(self.host + 'api/' + self.key + '/update/' + sub + '/' + pred + '/' + old_obj + ',' + new_obj)
	  		result = json.loads(content.text)
	  		if result['status'] != 100:
	  			raise '[COEUS] unable to update triple: ' 
	  		else:
	  			return True

	def delete(self,sub, pred, obj):
		if self.key == '':
  			raise '[COEUS] undefined API key'
  		else:
	  		content = requests.get(self.host + 'api/' + self.key + '/delete/' + sub + '/' + pred + '/' + obj)
	  		
	  		result = json.loads(content.text)
	  		if result['status'] != 100:
	  			raise '[COEUS] unable to delete triple: '
	  		else:
	  			return True

	def search(self,query):
		content = requests.get(self.host + 'textsearch/query='+query)
  		result = json.loads(content.text)
  		return result




