from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
    def _find(self, area_id: str) -> str:
        for country in self.__data:
            if country.id == area_id:
                return [country]
            for subject in country.areas:
                if subject.id == area_id:
                    return [country, subject]
                for city in subject.areas:
                    if city.id == area_id:
                        return [country, subject, city]
    def _apply_geocoding(self, area_id: str) -> str:
        f = self._find(area_id)
        return ", ".join(x.name for x in f)



        """
            TODO:
            - Сделать перебор дерева для каждого area_id
            - В ходе перебора возвращать массив элементов, состоящих из TreeNode необходимой ветки
            - Из массива TreeNode составить полный адрес
        """
