class LatLon:
	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon
        
class Waypoint(LatLon):
	def __init__(self, name, lat, lon):
		super().__init__(lat, lon)
		self.name = name

	def __str__(self):
		return '%s >> lat: %f, lon: %f' % (self.name, self.lat, self.lon)

class Geocache(Waypoint):
	def __init__(self, name, diff, size, lat, lon):
		super().__init__(name, lat, lon)
		self.diff = diff
		self.size = size

	def __str__(self):
		# return '%s >> difficulty: %2.1f, size: %d << lat: %f, lon: %f' % (self.name, self.diff, self.size, self.lat, self.lon)
		return F'{self.name} >> difficulty: {self.diff}, size: %d << lat: %f, lon: %f' % (self.name, self.diff, self.size, self.lat, self.lon)


waypoint = Waypoint("Catacombs", lat=41.70505, lon=-121.51521)
print(waypoint)

geocache = Geocache("Newberry Views", diff=1.5, size=2, lat=44.052137, lon=-121.41556)
print(geocache)
