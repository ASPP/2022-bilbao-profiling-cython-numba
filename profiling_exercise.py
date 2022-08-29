# adding to string

# adding to list

# list comprehensions vs for loop?

# permission vs forgivenes

# lots of unnecessary function calls (pass aggregates rather than single values)

# checking membership in list vs set

# optimizing double if statement

# preallocating lists

# for i in range(len(iterable)) vs for item in iterable

# import statements

# not using builtins

import collections
import re


def read_file(fn):
    words = []
    with open(fn, "r") as f:
        for l in f:
            for w in l.split():
                words.append(w)
                # words = words + [w]
    return words


def clean_words(words):
    forbidden_characters = ".,?!;:()"
    cleaned_words = []
    for w in words:
        cleaned_w = ""
        for c in w:
            if c not in forbidden_characters:
                cleaned_w += c
        cleaned_words.append(cleaned_w.lower())
    return cleaned_words


def count_words(words):
    counter = collections.defaultdict(int)
    for w in words:
        counter[w] += 1
    return counter


def sort_words_by_count(wc):
    return sorted(wc.items(), key=lambda t: t[1], reverse=True)


def save_word_count(wc):
    s = "\n".join(f"{t[0]},{t[1]}" for t in wc)
    with open("word_count.txt", "w") as f:
        f.write(s)


def main():
    words = read_file("./origin.txt")
    words = clean_words(words)
    wc = count_words(words)
    wc = sort_words_by_count(wc)
    save_word_count(wc)


if __name__ == "__main__":
    for _ in range(20):
        main()
