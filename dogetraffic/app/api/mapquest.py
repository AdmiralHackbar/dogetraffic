__author__ = 'maestro'
import json
import urllib2
from dogtraffic.settings_local import MAPQUEST_KEY


def getIncidents():
    # Hardcoded to Austin, TX
    data = json.load(urllib2.urlopen('http://www.mapquestapi.com/traffic/v2/incidents?key=' + MAPQUEST_KEY + '&boundingBox=30.505657,-98.018088,30.031230,-97.468771&filters=construction,incidents&inFormat=kvp&outFormat=json'))
    return data


def getMapImage(width, height):
    data = urllib2.urlopen('http://www.mapquestapi.com/staticmap/v4/getmap?key=' + MAPQUEST_KEY + '&size=' + str(width) + ',' + str(height) + '&zoom=10&center=30.268729930878855,-97.74342947489849')
    return data

