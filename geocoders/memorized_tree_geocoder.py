from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

        self.d = {}
        for country in self.__data:
            self.d[country.id] = [country.name]
            for subject in country.areas:
                self.d[subject.id] = [country.name, subject.name]
                for city in subject.areas:
                    self.d[city.id] = [country.name, subject.name, city.name]
    def _apply_geocoding(self, area_id: str) -> str:
        return ", ".join(self.d[area_id])

