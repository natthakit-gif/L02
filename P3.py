def survive_mars(area, depth):
    # Convert depth from cm to m
    depth_m = depth / 100
    # Calculate the soil volume in cubic meters
    soil_volume = area * depth_m
    # Calculate the total water required in liters
    water_required = soil_volume * 40
    return water_required

if __name__ == '__main__':
    w = survive_mars(126, 30)
    print('water', w, 'L')

    w = survive_mars(150, 40)
    print('water', w, 'L')

    w = survive_mars(100, 35)
    print('water', w, 'L')
