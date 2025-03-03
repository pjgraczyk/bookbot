from typing import Dict


def count_words(contents: str) -> int:
    return len(contents.split())


def get_letter_counts(contents: str):
    letter_count_dict = {}
    for char in contents.lower():
        if char.isalpha():
            letter_count_dict[char] = letter_count_dict.get(char, 0) + 1
    return letter_count_dict


def get_formatted_letter_counts(dict_counts: Dict) -> Dict:
    return dict(sorted(dict_counts.items(), key=lambda x: x[1], reverse=True))
