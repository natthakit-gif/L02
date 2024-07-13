def collect_data():
    observations = []
    counts = []

    while True:
        observation = input("Observation:")
        if observation == "":
            break

        try:
            count = int(input("Found:"))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        observations.append(observation)
        counts.append(count)

    return observations, counts

if __name__ == '__main__':
    observ, counting = collect_data()
    print(observ)
    print(counting)
