from profiling_exercise import clean_words, count_words, sort_words_by_count


def test_clean_words():
    words = ["test.", "test,test", "test123", "loud!", "question?"]
    cleaned_words = clean_words(words)
    expected = ["test", "testtest", "test123", "loud", "question"]
    assert cleaned_words == expected


def test_count_words():
    words = [
        "test",
        "testtest",
        "test123",
        "loud",
        "question",
        "test",
        "test",
        "test123",
    ]
    wc = count_words(words)
    expected = [
        ("test", 3),
        ("testtest", 1),
        ("test123", 2),
        ("loud", 1),
        ("question", 1),
    ]
    assert wc == expected


def test_sort_words_by_count():
    wc = [("test", 3), ("testtest", 1), ("test123", 2), ("loud", 1), ("question", 1)]
    sorted_wc = sort_words_by_count(wc)
    expected = [
        ("test", 3),
        ("test123", 2),
        ("testtest", 1),
        ("loud", 1),
        ("question", 1),
    ]
    assert sorted_wc == expected
