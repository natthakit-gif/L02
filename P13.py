def est_prob(counting):
    total_count = sum(counting)
    if total_count == 0:
        return [0] * len(counting)
    return [count / total_count for count in counting]

if __name__ == '__main__':
    counting = list(map(int, input("Enter the counts separated by spaces: ").split()))
    probabilities = est_prob(counting)
    print(probabilities)
