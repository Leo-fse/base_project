from collections import Counter


def get_number_with_highest_count(counts):
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            get_number_with_highest_count = number
    return get_number_with_highest_count


def most_frequent(numbers):
    counts = Counter(numbers)

    return get_number_with_highest_count(counts)
