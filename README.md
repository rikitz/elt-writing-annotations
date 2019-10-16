# elt-writing-annotations
Rendering schema of codes used by ELT teachers to correct learner writing in RDF/OWL, mapping them in a single ontology 

To query with SPARQL, publish as endpoint with Apache Jena Fuseki: eg

cd apache-jena-3.12.0

fuseki-server --update --mem /ds


Example SPARQL queries:

Return all classes:

SELECT  ?class ?label ?description
WHERE {
  ?class a owl:Class.
  OPTIONAL { ?class rdfs:label ?label}
  OPTIONAL { ?class rdfs:comment ?description}

}


Return a class  by name:

prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?class ?label ?description
WHERE {
  ?class a owl:Class.
  OPTIONAL { ?class rdfs:label ?label}
  OPTIONAL { ?class rdfs:comment ?description}
  FILTER (regex(str(?label), "Tagset"))
}


Return  individuals:

SELECT  ?individual ?label ?description
WHERE {
  ?class a owl:NamedIndividual.
  OPTIONAL { ?class rdfs:label ?label}
  OPTIONAL { ?class rdfs:comment ?description}
  FILTER (regex(str(?label), "M"))
}






