from geocoders.geocoder import Geocoder
from api import API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        d = API.get_area(area_id)
        name = d.name
        while d.parent_id is not None:
            d = API.get_area(d.parent_id)
            name = d.name + ", " + name
        return name