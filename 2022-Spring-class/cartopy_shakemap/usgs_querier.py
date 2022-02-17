"""

Class to query USGS events

@author: kongqk
"""

import csv
import requests
import pandas as pd

class EQFromUSGS(object):
  """Query USGS to get EQ info."""
  BASE = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&'
  
  def __repr__(self):
    return 'query USGS via ' +  EQFromUSGS.BASE

  
  @staticmethod
  def query_url(url):
    """
    Query USGS event with a URL. 

    Args:
      url (string): the query URL.

    Returns:
      earthquake: The pandas dataframe of the event.

    """
    
    # request event information from usgs by using the event id
    r = requests.get(url)
    text = (line.decode('utf-8') for line in r.iter_lines())
    # the first row will be header
    # data is in the 2nd row
    event_info = list(csv.reader(text))
    
    # header: ['time', 'latitude', 'longitude', 'depth', 'mag', 'magType',
    #          'nst', 'gap', 'dmin', 'rms', 'net', 'id', 'updated', 'place',
    #          'type', 'horizontalError', 'depthError', 'magError', 'magNst',
    #          'status', 'locationSource', 'magSource']
    earthquake = pd.DataFrame(event_info[1:], columns=event_info[0])
        
    return earthquake

  @staticmethod
  def from_evid(evid):
    """
    Query USGS by providing an event id. 

    Args:
      evid (string): USGS event id, i.e. 'us70006ara'.

    Returns:
      event (dataframe): dataframe contain all the events.

    """
    url = EQFromUSGS.BASE + 'eventid=' + evid
    event = EQFromUSGS.query_url(url)
    return event

  @staticmethod
  def from_time_range(starttime, 
                      endtime, 
                      min_mag=4., 
                      max_mag=9.):
    """
    Query USGS by providing a time range and magnitude range. 

    Args:
      starttime (string): starttime of the search, i.e. 2018-01-01.
      endtime (string): endtime of the search, i.e. 2018-02-01.
      min_mag (float, optional): Minimum magnitude. Defaults to 4.
      max_mag (float, optional): Maximum magnitude. Defaults to 9.

    Returns:
      events (dataframe): dataframe contain all the events.

    """
    url = (f'{EQFromUSGS.BASE}starttime={starttime}'
           f'&endtime={endtime}&minmagnitude={min_mag}'
           f'&maxmagnitude={max_mag}')
    events = EQFromUSGS.query_url(url)
    
    return events

  @staticmethod
  def from_time_space_rect(starttime, 
                           endtime, 
                           llat_degree, 
                           ulat_degree, 
                           llon_degree, 
                           ulon_degree, 
                           min_mag=4, 
                           max_mag=9):
    """
    

    Args:
      starttime (string): starttime of the search, i.e. 2018-01-01.
      endtime (string): endtime of the search, i.e. 2018-02-01.
      llat_degree (float): lower bound latitude in degree.
      ulat_degree (float): upper bound latitude in degree.
      llon_degree (float): lower bound longitude in degree.
      ulon_degree (float): upper bound longitude in degree.
      min_mag (float, optional): Minimum magnitude. Defaults to 4.
      max_mag (float, optional): Maximum magnitude. Defaults to 9.

    Returns:
      events (dataframe): dataframe contain all the events.

    """
    url = (f'{EQFromUSGS.BASE}starttime={starttime}&endtime={endtime}'
           f'&minlatitude={llat_degree}&maxlatitude={ulat_degree}'
           f'&minlongitude={llon_degree}&maxlongitude={ulon_degree}'
           f'&minmagnitude={min_mag}&maxmagnitude={max_mag}')
    event = EQFromUSGS.query_url(url)
    return event

  @staticmethod
  def from_time_space_circle(starttime, 
                             endtime, 
                             lat_degree, 
                             lon_degree, 
                             radius_km,
                             min_mag=4, 
                             max_mag=9):
    """
    

    Args:
      starttime (string): starttime of the search, i.e. 2018-01-01.
      endtime (string): endtime of the search, i.e. 2018-02-01.
      lat_degree (float): latitude of the center of the circle in degree.
      lon_degree (float): longitude of the center of the circle in degree.
      radius_km (float): radius of the circle in km.
      min_mag (float, optional): Minimum magnitude. Defaults to 4.
      max_mag (float, optional): Maximum magnitude. Defaults to 9.

    Returns:
      events (dataframe): dataframe contain all the events.

    """
    url = (f'{EQFromUSGS.BASE}starttime={starttime}&endtime={endtime}'
           f'&latitude={lat_degree}&longitude={lon_degree}'
           f'&maxradiuskm={radius_km}&minmagnitude={min_mag}'
           f'&maxmagnitude={max_mag}')
    events = EQFromUSGS.query_url(url)
    return events
