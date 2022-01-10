from collections import Counter


def get_number_with_highest_count(counts):
    return max(
        counts,
        key=lambda number: counts[number]
        # 第2引数keyの値としてnumberを引数として受け取りcounts[number]を返す関数を指定
    )


def most_frequent(numbers):
    counts = Counter(numbers)

    return get_number_with_highest_count(counts)
