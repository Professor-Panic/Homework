class House:
    bedrooms=3
    bathrooms=2
    floors=1
    area=120
    owner=None
    location=None
    architect="Tedd"
My_house=House()
My_house.owner="Tedd"
Bungalow=House()
Bungalow.floors=2
Bungalow.architect="Edwin"

print(f"My bathrooms       {My_house.bathrooms}")
print(f"My_bedrooms        {My_house.bedrooms}")
print(f"My Floors          {My_house.floors}")
print(f"Architect          {My_house.architect}")

print(f"Bungalow bathrooms {Bungalow.bathrooms}")
print(f"Bungalow_bedrooms  {Bungalow.bedrooms}")
print(f"Bungalow Floors    {Bungalow.floors}")
print(f"Bungalow Architect {Bungalow.architect}")