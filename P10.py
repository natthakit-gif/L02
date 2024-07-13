def clock_to_degree(clock):
    hour, minute = map(int, clock.split(':'))
    degree = (hour % 12) * 30 + (minute * 0.5)
    return degree

def sailing_strategy(wind_deg, heading_deg):
    normalize = (heading_deg - wind_deg + 360) % 360

    if normalize == 0:
        return "run"
    elif 0 < normalize < 90:
        return "starboard broad reach"
    elif normalize == 90:
        return "starboard beam reach"
    elif 90 < normalize < 135:
        return "starboard close hauled"
    elif 135 <= normalize <= 225:
        return "tacking"
    elif 225 < normalize < 270:
        return "port close hauled"
    elif normalize == 270:
        return "port beam reach"
    elif 270 < normalize < 360:
        return "port broad reach"

def sailor_mate(wind_clock, heading_clock):
    wind_deg = clock_to_degree(wind_clock)
    heading_deg = clock_to_degree(heading_clock)
    return sailing_strategy(wind_deg, heading_deg)

if __name__ == '__main__':
    r = sailor_mate("9:00", "12:00")
    print("9:00", "12:00", r) 

    ticks = ["12:00", "1:30", "1:31", "2:59", "3:00", "3:01", "5:59", "6:00", "6:01", "8:59", "9:00", "9:01", "10:29", "10:30"] 
    for b in ticks: 
        r = sailor_mate("6:00", b) 
        print("6:00", b, r)

