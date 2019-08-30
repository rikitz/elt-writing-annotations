import rdflib
g = rdflib.Graph()
result = g.parse("elt-writing-annotations.owl")

print("graph has %s statements." % len(g))
# prints graph has 79 statements.

for subj, pred, obj in g:
	print(subj, pred, obj)
	if (subj, pred, obj) not in g:
		raise Exception("It better be!")

s = g.serialize(format='n3')