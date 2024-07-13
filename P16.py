def typhoon(wspeed, adensity, area, height):
    # Convert wind speed from km/h to m/s
    wind_speed_m_s = wspeed / 3.6
    
    # Define storm categories
    storm_scale = [
        ('Category 5', 252),
        ('Category 4', 209),
        ('Category 3', 178),
        ('Category 2', 155),
        ('Category 1', 119),
        ('Tropical Storm', 63),
        ('Tropical Depression', 0)
    ]
    
    # Determine storm category
    for category, speed in storm_scale:
        if wspeed >= speed:
            storm_category = category
            break
    
    # Calculate effective area in square meters
    area_m2 = area * 1e6
    
    # Calculate air mass
    air_mass = adensity * area_m2 * height
    
    # Calculate kinetic energy
    energy = 0.5 * air_mass * wind_speed_m_s ** 2
    
    return [storm_category, energy]

if __name__ == '__main__':
    wspeed = float(input("Enter the wind speed (in km/h): "))
    adensity = float(input("Enter the air density (in kg/m³): "))
    area = float(input("Enter the effective area (in km²): "))
    height = float(input("Enter the effective height (in m): "))
    
    result = typhoon(wspeed, adensity, area, height)
    print(result)
