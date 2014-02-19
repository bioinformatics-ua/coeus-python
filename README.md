COEUS python  (non official client)
================================================================


## Installation

You will need to install the python dependencies:

    pip install -r requirements.txt




Install it yourself as:

    $ pip install coeus

## Usage

```python
# define COEUS base host address
c = coeus.COEUS( "uavr", "http://localhost:8080/coeus/")
``` 


```python
# execute SPARQL query on COEUS host
# returns RDF::Query::Solution array
c.query('SELECT * {?s ?p ?o}')
```

```python
# get triples from COEUS knowledge base (http://bioinformatics.ua.pt/coeus/documentation/#rest)
# returns array with binded objects
 c.triple('coeus:concept_BBC', 'p', 'obj')
```


```python
# write triples to COEUS knowledge base (http://bioinformatics.ua.pt/coeus/documentation/#rest)
# returns true if data written
c.write('coeus:python_x','dc:title','python_x')
```

```python
# updates triple in COEUS knowledge base (http://bioinformatics.ua.pt/coeus/documentation/#rest)
# returns true if data updated
c.update('coeus:python_x','dc:title','python_x', 'coeus-python')

```

```python
# delete triple from COEUS knowledge base (http://bioinformatics.ua.pt/coeus/documentation/#rest)
# returns true if data deleted
c.delete('coeus:python_x','dc:title','coeus-python')
```


```python
# search in free text #ALPHA #TESTING
# returns the triple results
c.search('Nanopublications')
```



## Contact
Luis A. Bastiao Silva - bastiao at ua dot pt

Based on https://github.com/bioinformatics-ua/coeus-gem (by Pedro Lopes)
