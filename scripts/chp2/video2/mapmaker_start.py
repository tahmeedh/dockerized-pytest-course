class Point():
    def __init__(self, name, lat, longit):
        self._name = name
        self._lat = lat
        self._long = longit
    
    def get_lat_long(self):
        return(self._lat , self._long)