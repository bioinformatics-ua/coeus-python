# -*- coding: utf-8 -*-


import coeus 


c = coeus.COEUS( "uavr", "http://localhost:8080/coeus/")
print c.triple('coeus:concept_BBC', 'p', 'obj')
print c.query("PREFIX coeus: <http://bioinformatics.ua.pt/coeus/resource/>\nSELECT COUNT(DISTINCT ?tag)  { ?tag coeus:hasConcept coeus:concept_BBC}")
#print c.write('coeus:gem_x','dc:title','gem_x')
#print c.update('coeus:gem_x','dc:title','gem_x', 'coeus-gem')
#print c.delete('coeus:gem_x','dc:title','coeus-gem')