class City:
    def __init__(self, city_name="", region_name="", country_name="", population="", zip_code="", area_code=""):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.population = population
        self.zip_code = zip_code
        self.area_code = area_code

    def input_data(self):
        self.city_name = input('City: ')
        self.region_name = input('Region: ')
        self.country_name = input('Country: ')
        self.population = input('Population: ')
        self.zip_code = input('Zip-code: ')
        self.area_code = input('Area-code: ')

    def output_data(self):
        print(f'\nCity: {self.city_name}')
        print(f'Region: {self.region_name}')
        print(f'Country: {self.country_name}')
        print(f'Population amount: {self.population}')
        print(f'Zip-code: {self.zip_code}')
        print(f'Area-code: {self.area_code}')


my_city = City()
my_city.input_data()
my_city.output_data()

