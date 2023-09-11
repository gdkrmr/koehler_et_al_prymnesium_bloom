#! /usr/bin/env python
import cdsapi
from os.path import exists
import sys

c = cdsapi.Client()

def retrievefull(y):
    filename = f'discharge_{y}_full.nc.zip'
    if not exists(filename):
        c.retrieve(
            'efas-historical',
            {
                'system_version': 'version_4_0',
                'variable': 'river_discharge_in_the_last_6_hours',
                'model_levels': 'surface_level',
                'hyear': str(y),
                'hmonth': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                ],
                'hday': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'time': [
                    '00:00', '06:00', '12:00',
                    '18:00',
                ],
                'format': 'netcdf',
            },
            filename)

def retrieve(y):
    filename = f'discharge_{y}.nc.zip'
    if not exists(filename):
        c.retrieve(
            'efas-historical',
            {
                'format': 'netcdf',
                'system_version': 'version_4_0',
                'variable': 'river_discharge_in_the_last_6_hours',
                'model_levels': 'surface_level',
                'hyear': str(y),
                'hmonth': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                ],
                'hday': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',
                ],
                'time': [
                    '00:00', '06:00', '12:00',
                    '18:00',
                ],
                'area': [
                    54, 14, 49,
                    20,
                ],
            },
            filename)


def main():
    y = int(sys.argv[1])
    print(f"downloading year {y}")
    #### there was a cropping issue on cds and retrieving cropped data for efas
    #### 4.0 was disabled. copernicus hasn't fixed the issue until 7/9/2023.
    #### Therefore we need to retrieve the full data and crop it manually. Each
    #### full netcdf file is >5GB in size! while the cropped files were < 70Mb
    #### each!
    retrievefull(y)
    # retrieve(y)

main()
