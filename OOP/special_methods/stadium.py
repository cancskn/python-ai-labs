class Stadium:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.name}, built in {self.year}"

stad1 = Stadium("PGE", 1986)
print(stad1)

