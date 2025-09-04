class Stadium:
    all_stadiums = []

    def __init__(self, name, date_opening=0, country='', city='', capacity=0):
        self.name = name
        self.date_opening = date_opening
        self.country = country
        self.city = city
        self.capacity = capacity
        Stadium.all_stadiums.append(self)

    @classmethod
    def add_stadium(cls):
        name = input('Stadium name: ')
        more = input('Do you want to add more details? (y/n): ').lower()

        if more == 'y':
            date_opening = int(input('Year of opening: '))
            country = input('Country: ')
            city = input('City: ')
            capacity = int(input('Capacity: '))
            cls(name, date_opening, country, city, capacity)
        else:
            cls(name)

    @classmethod
    def show_all(cls):
        if not cls.all_stadiums:
            print('No stadium found')
            return
        for stad in cls.all_stadiums:
            print(f'{stad.name}')

    @classmethod
    def filter_stadiums(cls):
        filter_key = input('Type "city" or "country" to filter the stadiums: ').lower()
        if filter_key == 'city':
            city = input('Enter city name: ').lower()
            for stad in cls.all_stadiums:
                if stad.city.lower() == city:
                    if stad.capacity:
                        print(f'{stad.name} with {stad.capacity} seats')
                    else:
                        print(f'{stad.name}')
                else:
                    print(f'No stadiums found in {city}')
        elif filter_key == 'country':
            country = input('Enter the country: ').lower()
            for stad in cls.all_stadiums:
                if stad.country.lower() == country:
                    if stad.capacity:
                        print(f'{stad.name} with {stad.capacity} seats')
                    else:
                        print(f'{stad.name}')
                else:
                    print(f'No stadiums found in {country}')

if __name__ == "__main__":
    stad = Stadium('PGE Narodowy', 2015, 'Poland', 'Warsaw', 58000)

    print('Menu:')
    print('1 - add stadiums')
    print('2 - show all stadiums')
    print('3 - search stadium by city/country')
    print('0 - exit')

    while True:
        choice = int(input('Enter your choice(0-3): '))
        if choice == 1:
            Stadium.add_stadium()
        elif choice == 2:
            Stadium.show_all()
        elif choice == 3:
            Stadium.filter_stadiums()
        elif choice == 0:
            break



