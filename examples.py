# -*- coding: utf-8 -*-

# Copyright 2013, Luís Bastião Silva, Universidade de Aveiro
# Authors: Luis A. Bastiao Silva <luis.kop@gmail.com> 


import coeus 


c = coeus.COEUS( "uavr", "http://localhost:8080/coeus/")
print c.triple('coeus:concept_BBC', 'p', 'obj')
print c.write('coeus:gem_x','dc:title','gem_x')
print c.update('coeus:gem_x','dc:title','gem_x', 'coeus-gem')
print c.delete('coeus:gem_x','dc:title','coeus-gem')
print c.query("PREFIX coeus: <http://bioinformatics.ua.pt/coeus/resource/>\nSELECT COUNT(DISTINCT ?tag)  { ?tag coeus:hasConcept coeus:concept_BBC}")
print c.query("PREFIX coeus: <http://bioinformatics.ua.pt/coeus/resource/> SELECT * { ?s ?p ?o }")
print c.search("Nanopublications")