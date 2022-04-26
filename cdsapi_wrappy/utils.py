import os
import json
import numpy as np

###############################################################################


def load_databases():
    """
    load preset configuration for a few databases, like single-levels from the ECMWF
    
    :returns: dict
        dictionary with databases as keys
    """
    cdir = os.path.dirname(os.path.abspath(__file__))
    json_file = open(f"{cdir}/database_parameters.json", "r")
    databases = json.load(json_file)
    
    return databases

###############################################################################


def formatting_date(varb, digits=2, time_fmt='hour'):
    """
    """
    if time_fmt == 'hour':
        suffix = ":00"
    else:
        suffix = ""
    
    # checking the secondary variables now
    if type(varb) in [str, int, float]:
        varb = str(varb).zfill(digits)
    elif type(varb) in [list, np.ndarray]:
        varb = [f'{str(y).zfill(digits)}{suffix}' for y in varb]
    else:
        varb = '2019'
        
    return varb

###############################################################################


