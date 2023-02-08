# cdsapi_wrappy
A python wrapper for cdsapi


# Installation

Requirements:
- numpy
- cdsapi
- pandas


## Install the CDS API client 
(Instructions copied from: https://cds.climate.copernicus.eu/api-how-to
)
- The CDS API client is a python based library. It provides support for both Python 2.7.x and Python 3.

- You can Install the CDS API client via the package management system pip, by running on Unix/Linux the command shown in the box below.

    ```
    pip install cdsapi
    ```
### Register
1. If you don't have an account, please self register at the [CDS registration page](https://cds.climate.copernicus.eu/user/register?destination=%2F%23!%2Fhome) and go to the steps below.
If you are not logged, please login and go to the step below.

2. If you are not logged, please login and go to the step below.

3. Copy the code displayed below, in the file $HOME/.cdsapirc (in your Unix/Linux environment).
    ```
    url: https://cds.climate.copernicus.eu/api/v2
    key: {uid}:{api-key}
    ```

## Install cdsapi_wrappy
- You can install cdsapi_wrappy by running:
    ```
    git clone https://github.com/lhico/cdsapi_wrappy.git
    cd cdsapi_wrappy
    git checkout 1_hotfix-hard-coded-values-in-build_request
    pip install .
    ```
## Download example:
This is an example of the package usage. Other examples are in the `notebooks` directory.

```
import cdsapi_wrappy as cds
import numpy as np


request = cds.build_request("reanalysis-era5-single-levels",
                     {'latN':-20, 'lonW':-55, 'latS':-35,'lonE':-35},
                     2019,
                     7,
                     np.arange(31),
                     ["00:00"],
                     ["10m_u_component_of_wind", "10m_v_component_of_wind",
                      "2m_temperature", "mean_sea_level_pressure",
                      "sea_surface_temperature", "total_precipitation",
                      "surface_latent_heat_flux", "surface_sensible_heat_flux",
                      "surface_solar_radiation_downwards", "evaporation",
                      "2m_dewpoint_temperature"],
                      product_type =  "reanalysis",
                       format="netcdf")

cds.request_cdsapi(request=request)
```


