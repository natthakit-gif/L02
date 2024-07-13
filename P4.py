def martian_botanist(sols, daily_consumption, production_per_area):
    # Calculate total potato needed (in kg)
    total_potato_needed = sols * daily_consumption
    # Calculate planting area (in m²)
    planting_area = total_potato_needed / production_per_area
    return planting_area

if __name__ == '__main__':
    area = martian_botanist(150, 2, 2.4)
    print('planting area:', area, 'sq. m.') 

    area = martian_botanist(900, 2.5, 1.2) 
    print('planting area:', area, 'sq. m.') 

    area = martian_botanist(200, 2.4, 1.6) 
    print('planting area:', area, 'sq. m.')