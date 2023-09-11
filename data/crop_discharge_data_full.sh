#! /bin/bash

LONMIN=14
LONMAX=20
LATMIN=49
LATMAX=54

for f in *_full.nc;
do
    echo "cropping $f, output ${f%_full.nc}_cropped.nc"
    cdo \
        -sellonlatbox,$LONMIN,$LONMAX,$LATMIN,$LATMAX \
        "$f" \
        "${f%_full.nc}_cropped.nc"
    echo "done"
done
