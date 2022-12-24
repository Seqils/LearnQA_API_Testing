def test_short_phrase():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, f"Phrase in longer then 15 chars. Have {len(phrase)}"


