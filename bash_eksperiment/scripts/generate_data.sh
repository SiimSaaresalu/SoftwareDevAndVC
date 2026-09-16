#!/bin/bash

# Käivitab generate_data.py skripti 10 korda.

N=10

for i in $(seq 1 "$N")
do
	py generate_data.py > "../data/data${i}.txt"
done

echo "Failid genereeritud data/ kataloogi"

