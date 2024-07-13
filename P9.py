def count_kmer(kmer, text):
    count = 0
    k = len(kmer)
    for i in range(len(text) - k + 1):
        if text[i:i+k] == kmer:
            count += 1
    return count

if __name__ == '__main__':
    kmer = input()
    text = input()
    result = count_kmer(kmer, text)
    print(result)