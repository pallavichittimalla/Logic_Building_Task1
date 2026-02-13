# Simple Data Cleaner

def clean_names(names):
    cleaned = []

    for name in names:
        cleaned.append(name.strip().lower())

    return cleaned


if __name__ == "__main__":
    names = [" Alice ", "bob", " CHARLIE "]
    print(clean_names(names))
