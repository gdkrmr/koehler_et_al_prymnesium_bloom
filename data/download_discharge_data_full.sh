#! /bin/bash

for i in {1991..2022}; do
    echo "requesting year $i"
    pyenv/bin/python download_discharge_data_cli.py $i &
done
