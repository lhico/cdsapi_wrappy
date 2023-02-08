import numpy as np
import cdsapi

from .utils import formatting_date, load_databases

###############################################################################


def build_request(database, area, year, month, day, hour, 
                  variables=None, product_type=None,
                  format=None):
    """
    
    variables, product_type and format are primary variables, needed if you
    are trying to build a request from scratch
    
    database, area, year, month, day, hour are secondary variables, used to 
    request a specific region and period of data
    
    """
    
    # loading preset if available
    databases = load_databases()
    
    if database in databases.keys():
        # if database exist, then load this dictionary
        request = databases[database]
        
    else:
        # checking if important variables were sent as argument to create a
        # request from scratch
        if format and product_type and database and variables:
            print(f'Creating a request from scratch using {database} and {format}/{product_type}')
            
            # build the dictionary using the primary variables sent
            request = {
                        'format': format,
                        'product_type': product_type,
                        'variables': variables
                      }
        else:
            warning_msg = "This database is not in database_parameters.json. You can either add this database in the file or create a request from scratch by passing the right variables."
            raise Warning(warning_msg)
    
    # checking the secondary variables now
    year = formatting_date(year, digits=4)
    month = formatting_date(month, digits=2)
    day = formatting_date(day, digits=2, time_fmt='day')
    hour = formatting_date(hour, digits=2)
    
    request['year'] = year
    request['month'] = month
    request['day'] = day
    request['time'] = hour
    request['area'] = [area['latN'],area['lonW'],area['latS'],area['lonE']]
    request['variable'] = variables
    
    return request
    
###############################################################################


def request_cdsapi(request=None, 
                   name="reanalysis-era5-single-levels", 
                   target="download.nc"):
    """
        adicionar date como argumento, para receber year/month/day/time
    """
    
    assert (type(request) == dict), "request must be a valid dictionary. Check the documentation to know more"

    c = cdsapi.Client()

    c.retrieve(name, request, target=target)

###############################################################################
