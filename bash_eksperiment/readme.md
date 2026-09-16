# Bash eksperiment

Harjutati käsureatööriistade kasutamist.

`scripts/generate_data.py` genereerib 200 juhuslikku äisarvu vahemikus 1..100.
Bahhi skript `scripts/generate_data.sh` käivitab Pythoni skripti 10 korda ja salvestab väljundid `data/` kataloogi.
Viimaks loendame unikaalsed arvud kokku genereeritud failides. Tulemus on failis `results/summary_total_unique_numbers_counted.txt`.

## Kasutatud käsud

```bash
mkdir bash_eksperiment
cd bash_eksperiment/
mkdir data scripts results
cd ..
cd bash_eksperiment/
touch readme.md
cd scripts/
vim generate_data.py
vim generate_data.sh
chmod +x generate_data.sh 
./generate_data.sh 
vim generate_data.sh
./generate_data.sh 
vim generate_data.sh
cd ..
cd data/
ls
wc -l data/*.txt
wc -l *.txt
cd ..
cat data/*.txt | sort -n | uniq -c > results/summary_total_unique_numbers_counted.txt
cat results/summary_total_unique_numbers_counted.txt 
vim readme.md 
