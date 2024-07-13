def laplace_smooth(counting, alpha):
    total_count = sum(counting)
    num_classes = len(counting)
    smoothed_prob = [(count + alpha) / (total_count + alpha * num_classes) for count in counting]
    return smoothed_prob

if __name__ == '__main__':
    counting = list(map(int, input("Enter the counts separated by spaces: ").split()))
    alpha = float(input("Enter the smoothing factor alpha: "))
    probabilities = laplace_smooth(counting, alpha)
    print(probabilities)
