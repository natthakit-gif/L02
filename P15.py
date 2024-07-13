import math

def earthquake(events):
    for event in events:
        magnitude = event[1]
        energy = 10 ** (4.8 + 1.5 * magnitude)
        event.append(energy)
    return events

if __name__ == '__main__':
    events = [
        ['2019 02 22 Ecuador', 7.5],
        ['2018 08 19 Fiji', 8.2],
        ['2017 09 08 Mexico', 8.2]
    ]
    result = earthquake(events)
    for event in result:
        print(event)
