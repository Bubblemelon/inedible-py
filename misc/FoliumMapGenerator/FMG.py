# data virtualization using Leaflet map
# https://pypi.org/project/folium/0.1.5/
import folium 
# any callable object can be treated as a function
import functools
import json
import logging
import os
# https://pypi.org/project/haversine/
# calculates the distance between 2 points using long and lat or (easting and northing)
from haversine import haversine

# global vars
STORE_LOCATION = (37.385, -122.089)
UNIT = 'km'

def parse_csv(file, delimiter):

    # open file with mode as read only
    with open(file, 'r') as f:

        # get all file lines
        lines = f.readlines()

        # strip(): removes both sides of the string matching the specified char.
        # if empty param, then removes leading and trailing spaces
        # split string by delimiter char
        # header == column names
        header = lines[0].strip().split(delimiter)

        # saves all entries starting from the first entry of the file
        # add each entry to the list/array 
        # entries = [ line.strip().split(delimiter) for line in lines[1:] ]
        #
        # https://stackoverflow.com/questions/6288016/generator-object-is-not-subscriptable-error
        # Python's "lists" are closer to arrays than to what most other languages would call a list. 
        # They're automatically-resizing arrays (which many language call "vectors" or even simply "arrays"). 
        # They're not linked lists, and they support constant-type lookup of any element, 
        # not just the head, unlike "lists" in most languages
        #
        # generator object
        # requires less memory than lists
        # same content as list ^^^ above line 29
        # see: https://stackoverflow.com/questions/5164642/python-print-a-generator-expression
        entries = ( line.strip().split(delimiter) for line in lines[1:] )


    # This is what zip does: https://www.w3schools.com/python/showpython.asp?filename=demo_ref_zip
    # generator object of dict objects
    # header: entry-val
    # result = ( dict(zip(header, [float_convert(e) for e in entry])) for entry in entries )

    # passing (data = result) into generate map does not work as a generator object
    result = [ dict(zip(header, [float_convert(e) for e in entry])) for entry in entries ]

    return result

# converts long and lat as floats and ignores other values e.g. string
def float_convert(input):
    try:
        return float(input)
    except ValueError:
        return input

# function closure
# https://www.programiz.com/python-programming/closure
def abbreviate(func):
    @functools.wraps(func)

    # *args is a tuple of parameter values
    # **kwargs is a dictionary of key/values
    # Take an arbitrary number of kwargs == keyword arguments
    def wrapper(*args, **kwargs):
        get_string_res = func(*args, **kwargs)
        return '{0} ...'.format(get_string_res[0:6])
    return wrapper

# function decorator
@abbreviate
def get_string(s):
    return s

# converts generator object of dictionary entries into JSON format
def jsonify(func):
    @functools.wraps(func)
    def wrapper_convert_to_json(**kwargs):
        datum = func(**kwargs)
        # https://macwright.org/2015/03/23/geojson-second-bite#features
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    datum['easting'],
                    datum['northing']
                ]
            },
            "properties": {
                "name:" "null island"
            }
        }
        feature['properties'] = datum
        return feature
    return wrapper_convert_to_json

# calculates distance between 2 points
@jsonify
def distance(p1, p2, u):
    x = p2['easting']
    y = p2['northing']
    # (lat,long)
    # http://www.satsig.net/world105.gif
    dist = haversine( p1, (y,x), unit=u)
    # add distance key value to dictionary entry from generator object
    p2['distance'] = dist
    return p2

# generate map via folium using coordinates
# https://python-visualization.github.io/folium/quickstart.html
def generate_map(center, features, data):

    # https://macwright.org/2015/03/23/geojson-second-bite#featurecollection 
    # features need to be a list
    fc = {
          "type": "FeatureCollection",
          "features": features
    }

    points = json.dumps(fc)

    # prints all points as JSON
    # print(points)

    # types of tiles: https://python-visualization.github.io/folium/modules.html
    m = folium.Map(
        location=center,
        tiles='OpenStreetMap',
        zoom_start=15
    )

    # https://python-visualization.github.io/folium/quickstart.html#GeoJSON/TopoJSON-Overlays
    # points must be in JSON format
    folium.GeoJson(
        points,
        name='geojson'
    ).add_to(m)

    tooltip = 'See who lives here!'

    folium.Marker(
        location = center,
        popup='Pet Store',
        icon=folium.Icon(color='green', icon='paw', prefix='fa'),
        tooltip='Hello!'
    ).add_to(m)

    # populate markers
    for d in data:

        if int(d['petcount']) == 0:
            temp = d['name'] + ' has no pets.'
            couleur = 'blue'
        elif int(d['petcount']) == 1:
            temp = d['name'] + ' has ' + str(int(d['petcount'])) + ' pet.'
            couleur = 'purple'
        else:
            temp = d['name'] + ' has ' + str(int(d['petcount'])) + ' pets.'
            couleur = 'darkpurple'

        folium.Marker(
            location = ( d['northing'],d['easting'] ),
            popup=temp,
            icon=folium.Icon(icon='home', color=couleur, prefix='fa'),
            tooltip=tooltip
        ).add_to(m)

    # to add layers on the map
    folium.LayerControl().add_to(m)

    # https://python-visualization.github.io/folium/quickstart.html#Getting-Started
    # saves the map to index.html in current dir 
    m.save('index.html')
    return m

def main():
    # locates the file "customers.txt" by taking current working dir and concatenate with /data/customers.txt
    file = os.path.join(os.getcwd(), 'data', 'customers.txt')
    data = parse_csv(file, '|')

    # print(data[0]) # TypeError: 'generator' object is not subscriptable

    # empty list
    features = []


    # for each dict the the generator object
    for d in data:

        # to create a list of tuples | access: names[i][0] == name && name[i][1] == petcount
        # names.append( (get_string(d['name']), d['petcount']) )

        # override to become JSON
        d = distance(p2=d, p1=STORE_LOCATION, u=UNIT)

        # take dict objects (JSON objects) from generator object and place into list
        features.append(d)
    
    generate_map(STORE_LOCATION, features, data)

if __name__ == '__main__':
    main()