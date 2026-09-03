class House:
    bedrooms=3
    bathrooms=2
    floors=1
    area=120
    owner=None
    location=None
    architect="Tedd"
    def __init__(self,owner,location):
        self.owner=owner
        self.location=location
    def print_self(self):
        print(self)
        print(self.__dict__)
My_house=House(owner="Tedd",location="Nairobi")
Bungalow=House(owner="Edwin",location="Nairobi")
Bungalow.floors=2
print(f"My bathrooms       {My_house.bathrooms}")
print(f"My_bedrooms        {My_house.bedrooms}")
print(f"My Floors          {My_house.floors}")
print(f"Architect          {My_house.architect}")

print(f"Bungalow bathrooms {Bungalow.bathrooms}")
print(f"Bungalow_bedrooms  {Bungalow.bedrooms}")
print(f"Bungalow Floors    {Bungalow.floors}")
print(f"Bungalow Architect {Bungalow.architect}")
My_house.print_self()
Bungalow.print_self()