import collections
import operator
import re


def read_file(fn):
    words = []
    with open(fn, "r") as f:
        for l in f:
            for w in l.split():
                words.append(w)
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
    counter = []
    for w in words:
        found = False
        for i in range(len(counter)):
            if w == counter[i][0]:
                counter[i][1] += 1
                found = True
                break
        if not found:
            counter.append([w, 1])
    wc = [tuple(t) for t in counter]
    return wc


def sort_words_by_count(wc):
    return sorted(wc, key=operator.itemgetter(1), reverse=True)


def save_word_count(wc):
    s = "\n".join(f"{t[0]},{t[1]}" for t in wc)
    with open("word_count.txt", "w") as f:
        f.write(s)


def main():
    words = read_file("./origin_chapter1.txt")
    words = clean_words(words)
    wc = count_words(words)
    wc = sort_words_by_count(wc)
    save_word_count(wc)


if __name__ == "__main__":
    for _ in range(10):
        main()
