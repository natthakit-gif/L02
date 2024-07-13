def perf_note(pnotes, evap_coeff):
    for note in pnotes:
        note_name, min_coeff, max_coeff = note
        if min_coeff <= evap_coeff <= max_coeff:
            return note_name
    return "Unknown"

if __name__ == '__main__':
    pnotes = [['head note', 1, 14], ['heart note', 15, 60], ['base note', 61, 100]]
    
    while True:
        try:
            evap_coeff = float(input("Enter the evaporation coefficient: "))
            note = perf_note(pnotes, evap_coeff)
            print(note)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            break
