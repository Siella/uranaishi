from collections import defaultdict
from typing import List


class Uranaishi:
    """
    Suggests autocompletions for word beginnings.
    """
    def __init__(self, file_path: str, encoding: str = 'utf-8'):
        self.word_freq = defaultdict(int)
        self.matches = defaultdict(list)

        with open(file_path, 'r', encoding=encoding) as f:
            N = int(f.readline())
            for _ in range(N):
                word, freq = f.readline().split(' ')
                self.word_freq[word] = int(freq)
            M = int(f.readline())
            for _ in range(M):
                char_seq = f.readline().rstrip('\n')
                self.matches[char_seq] = self.get_matches(char_seq)

    def get_matches(self, char_seq: str) -> List:
        """
        Gets up to ten word matches for the first letters
        ordered by term frequency and alphabet.

        :param char_seq: beginning of the word
        :return: list of matches for autocompletion
        """
        matches = {
            key: val for key, val in self.word_freq.items()
            if key.startswith(char_seq)
        }
        return sorted(
            matches,
            key=lambda key: (matches[key], key),
            reverse=True)[:10]


if __name__ == "__main__":
    u = Uranaishi('text.txt')
    for word in u.matches:
        print(*u.matches[word]+[''], sep='\n')
