PY=python3

testpagerank:
	${PY} src/testing.py

pagerank:
	${PY} src/test_pagerank.py file=${file}

collector:
	${PY} src/test_collector.py data=${data} dir=${dir} dict=${dict} ignore=${ignore} 

search:
	${PY} src/search.py words=${words}

