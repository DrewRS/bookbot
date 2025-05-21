def get_book_text(file):
    with open(file) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def dict_sort(chars):
    totals = []
    for c in chars:
        totals.append({"char": c, "num": chars[c]})
    totals.sort(reverse=True, key=sort_on)
    return totals