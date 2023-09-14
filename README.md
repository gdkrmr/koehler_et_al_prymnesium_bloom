# Oder Algae Bloom 2022 Spatiotemporal Chlorophyll and Discharge Analysis

## About
This repository contains the code used to generate the spatiotemporal
chlorophyll and discharge analysis for the 2022 Oder Algae Bloom.

## Data

- The chlorophyll data is available in the `data` folder.
  (`pixel_extraction_Oder_20220701_20220818_full_consolidated.txt`)
- The river network data is available in the `data` folder.
- The discharge data has to be downloaded from Copernicus Climate Data Store
  (CDS) and is not included in this repository (`data/discharge_{yyyy}_cropped.nc`)
  - The data can be downloaded using the `download.sh` script.
    - Downloading the data requires an API key for CDS.
    - For downloading, the python version in `pyenv` has been used. It contains
      the packages `cdsapi`
  - There are issues with downloading cropped data so we have to download the
    full data and crop it manually. For cropping `cdo` is required.

## Reproduce the analysis
### Required Data
- Download the runoff data with `data/download_discharge_data_full.sh`
  - The required python package is [cdsapi](https://cds.climate.copernicus.eu/toolbox/doc/index.html)
  - You also require an [API key](https://cds.climate.copernicus.eu/api-how-to#install-the-cds-api-key) for CDS.
  - Unzip the runoff data using `unzip_discharge_data_full.sh`
    - The data is quite large ~0.5TB after unzipping.
  - Crop the runoff data to size using `crop_discharge_data_full.sh`
    - requires [CDO](https://www.unidata.ucar.edu/software/netcdf/workshops/2012/third_party/CDO.html)
- River network data can be downloaded from
  [Inspire](https://inspire-geoportal.ec.europa.eu/download_details.html?view=downloadDetails&resourceId=%2FINSPIRE-d81e48c4-b4cf-11e3-a455-52540004b857_20230602-120602%2Fservices%2F1%2FPullResults%2F451-500%2Fdatasets%2F7&expandedSection=metadata)
  [here](https://wody.isok.gov.pl/atom_web/download/?fileId=107b702c828ca4d55f7317585ba016e8&name=RWB_2016_ManagementRestrictionOrRegulationZone_2020_L.zip).
- Chlorophyll data: `data/chlorophyll_data.csv`
  - Created by: Jorrit Scholze and Kerstin Stelzer, Brockmann Consult GmbH
  - License: The file data/chlorophyll_data.csv is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License http://creativecommons.org/licenses/by-nc/4.0/
- Measured discharge, data has to be requested
  (`data/6030800_Hohensaaten-Finow_Q_TagWerte.csv` and
  `data/6030000_Eisenhuettenstadt_Q_TagWerte.csv`): Department of Water
  Management 1, Brandenburg State Office for the Environment, 2022, Potsdam,
  Germany. Link: https://pegelportal.brandenburg.de
- City data
  - `oder_cities.geojson` and `oder_towns.geojson`.
  - Geographical location of relevant cities and towns.
  - Source: Open Street Map.
  - License: The files `data/oder_cities.geojson` and `data/oder_towns.geojson`
    are made available under the Open Database License:
    http://opendatacommons.org/licenses/odbl/1.0/. Any rights in individual
    contents of the database are licensed under the Database Contents License:
    http://opendatacommons.org/licenses/dbcl/1.0/


### Analysis

- See `data/.gitignore` for required files
- To reproduce the analysis compile `map2wave_supplement.Rmd` using the command

  ```sh
  Rscript -e "rmarkdown::render('map2wave_supplement.Rmd')"
  ```

  in the end of `map2wave_supplement.html` is a `sessionInfo()` output specifying
  all versions of R and R packages used

## License

- The code in this repository is GPL v3 licensed, see the file `[LICENSE](./LICENSE)`,
  datasets distributed with this repository have their own licenses, see
  [Required Data](./README.md#Required-Data) for details.


## Cite

Please cite as:

TODO!
