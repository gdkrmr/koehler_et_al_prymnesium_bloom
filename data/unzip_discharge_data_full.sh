#! /bin/bash

for f in *_full.nc.zip;
do
    echo "unzipping $f"
    unzip -p "$f" "mars_data_0.nc" > "${f%%.*}.nc" &
done
