import numpy as np
from cdsapi_wrappy.utils import load_databases
from cdsapi_wrappy.cdsapi_wrappy import request_cdsapi

# BEFORE STARTING, you need to configure:

# - check if the database you want to download is available at database_parameters.json.
#   if not, add this database.
# - scripts/

database =  'reanalysis-era5-single-levels'

# loading a preset for ERA5 single levels
request = load_databases()[database]

# filling request with your own need (region, period, variables, and so on)
request['year'] = '2019'
request['month'] = '01'
request['day'] = [f'{x:02d}' for x in np.arange(1,3,1)]
request['time'] = [f'{x:02d}:00' for x in np.arange(24)]
request['area'] = [10, -80, 10, -60]
request['variable'] = ['sea_surface_temperature']

print(request)

# perform the request
out_filename = "~/Downloads/downloading_test.nc"
request_cdsapi(request=request, name=database, target=out_filename)

