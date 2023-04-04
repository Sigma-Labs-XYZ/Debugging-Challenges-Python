# Write a function that takes a list of sentences (a book) and returns a list of (word, word, avg_proximity) tuples
# where avg_proximity is the mean distance (as a float) between two words in all sentences in the entire book.
# Ordered by avg_proximity smallest to largest, word_1, word_2. In "The red house" the distance between the and house is one.

# Your results should be case insensitive and there should only be one tuple per word-word pair.
# The first word in the tuple should be the smallest alphanumerically out of the pair.
#
# Note that if two words never occured in the same sentence together,
# they will not be in a record together in the list.

# Note that one word can be in a sentence more than once.

# See test case to understand output
from typing import List, Tuple, Set, Dict

Word = str
Sentence = List[Word]
Book = List[Sentence]
ProximityRecord = Tuple[Word, Word, float]


def get_proximity_records(book: Book) -> List[ProximityRecord]:
    def get_word_distances_for_sentence(
        sentence: Sentence,
    ) -> List[Tuple[Word, Word, int]]:
        word_distances: List[Tuple[Word, Word, int]] = []
        ids_considered: Set[Tuple[int, int]] = set()
        for i, word_1 in enumerate(sentence):
            for j, word_2 in enumerate(sentence):
                id = tuple(sorted((i, j)))

                if id in ids_considered:
                    continue

                ordered_words = tuple(sorted((word_1, word_2)))

                distance = abs(i - j)
                word_distances.append(ordered_words + (distance))
        return word_distances

    def reduce_word_distances(
        word_distances: List[Tuple[Word, Word, int]]
    ) -> List[ProximityRecord]:
        word_pair_counts_distances: Dict[
            Tuple[Word, Word], Tuple[int, int]
        ] = dict()  # {(word_1, word_2) : (count, sum_distance)}
        for word_1, word_2, distance in word_distances:
            count, sum_distance = word_pair_counts_distances.get(
                (word_1, word_2), (0, 0)
            )
            word_pair_counts_distances[(word_1, word_2)] = (
                count + 1,
                sum_distance + distance,
            )
        return [
            (word_1, word_2, count / sum_distance)
            for (word_1, word_2), (
                count,
                sum_distance,
            ) in word_pair_counts_distances.items()
        ]

    return sorted(
        reduce_word_distances(
            [
                word_distances
                for sentence in book
                for word_distances in get_word_distances_for_sentence(sentence)
            ]
        ),
        key=lambda proximity_record: (proximity_record[2]),
    )
