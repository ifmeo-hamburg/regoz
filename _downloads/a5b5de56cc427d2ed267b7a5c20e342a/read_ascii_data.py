import pandas as pd
import numpy as np
import xarray as xr

from datetime import date

# Define index ranges and constants
INDEX_RANGES = {
    'date'      : (1, 7),
    'depth'     : (9, 150),
    'lat'       : 150,
    'lon'       : 151,
    'direction' : (152, 292),
    'magnitude' : (293, 433)
}

def read_adcp_ascii_file(data_file: str, 
                         cruise: str = 'Unknown', 
                         station: str = 'Unknown', 
                         INDEX_RANGES: dict = {
                             'date'      : (1, 7),
                             'depth'     : (9, 150),
                             'lat'       : 150,
                             'lon'       : 151,
                             'direction' : (152, 292),
                             'magnitude' : (293, 433)
                         
                         },
                         NAN_VALUE: int = -32768
                        ) -> xr.Dataset:
    ''' Reads ADCP data from a given ASCII file and returns an xarray object '''

    # Read data from comma separated text file
    data = pd.read_csv(data_file, delimiter=',')

    # Extract columns using index ranges
    date_cols = data.columns[INDEX_RANGES['date'][0]:INDEX_RANGES['date'][1]]
    depth_cols = data.columns[INDEX_RANGES['depth'][0]:INDEX_RANGES['depth'][1]]
    lat_col = data.columns[INDEX_RANGES['lat']]
    lon_col = data.columns[INDEX_RANGES['lon']]
    direction_cols = data.columns[INDEX_RANGES['direction'][0]:INDEX_RANGES['direction'][1]]
    magnitude_cols = data.columns[INDEX_RANGES['magnitude'][0]:INDEX_RANGES['magnitude'][1]]

    # Select data by columns
    depth = data[depth_cols].values
    latitude = data[lat_col].values
    longitude = data[lon_col].values
    direction = data[direction_cols].values
    magnitude = data[magnitude_cols].values

    # Convert date to datetime object 
    date_str = data[date_cols].astype(str).agg(','.join, axis=1)
    dates = pd.to_datetime(date_str, format='%y,%m,%d,%H,%M,%S')      # 

    # Set a specific value which stands for NaN in direction + magnitude data
    direction = np.where(direction == NAN_VALUE, np.nan, direction)
    magnitude = np.where(magnitude == NAN_VALUE, np.nan, magnitude)
    
    # Select depth values of first row
    depth_values = depth[0][0:-1]

    # Create xarray structure
    ds = xr.Dataset(
        {
            'direction': (['time', 'depth'], direction),
            'magnitude': (['time', 'depth'], magnitude),
            'longitude': (['time'], longitude),
            'latitude': (['time'], latitude),
            'cruise': np.array(cruise.encode('utf-8')),
            'station': np.array(station.encode('utf-8')),
        },
        coords={
            'time': dates, 
            'depth': depth_values,
        },
    )

    return ds
    

