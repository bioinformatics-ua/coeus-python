


import coeus 


c = COEUS("http://bioinformatics.ua.pt/coeus", "coeus")
print c.triple()
print c.query("PREFIX coeus: <http://bioinformatics.ua.pt/coeus/resource/>\nSELECT COUNT(DISTINCT ?tag) { ?tag coeus:hasConcept coeus:concept_UniProt}")
print c.write('coeus:gem_x','dc:title','gem_x')
print c.update('coeus:gem_x','dc:title','gem_x', 'coeus-gem')
print c.delete('coeus:gem_x','dc:title','coeus-gem')