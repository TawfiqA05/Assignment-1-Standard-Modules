import random
import string
import os
from datetime import datetime

def generate_memorable_password(num_words=4, case='lower'):
    words_list = None
    nouns_file = 'top_english_nouns_lower_100000.txt'

    if os.path.isfile(nouns_file):
        with open(nouns_file, 'r', encoding='utf-8') as f:
            words_list = [w.strip() for w in f.readlines() if w.strip()]
    else:
        words_list = [
            'apple', 'river', 'mountain', 'table', 'computer',
            'plane', 'flower', 'notebook', 'music', 'bottle',
            'light', 'mirror', 'picture', 'phone', 'water'
        ]

    chosen_words = random.sample(words_list, k=num_words)

    if case.lower() == 'lower':
        chosen_words = [w.lower() for w in chosen_words]
    elif case.lower() == 'upper':
        chosen_words = [w.upper() for w in chosen_words]
    elif case.lower() == 'mixed':
        def random_case(word):
            return ''.join(random.choice([c.lower(), c.upper()]) for c in word)
        chosen_words = [random_case(w) for w in chosen_words]
    else:
        chosen_words = [w.lower() for w in chosen_words]

    chosen_words_with_digits = [w + str(random.randint(0, 9)) for w in chosen_words]
    return "-".join(chosen_words_with_digits)

def generate_random_password(length=12, include_punct=True, disallowed_chars=None):
    if disallowed_chars is None:
        disallowed_chars = []

    char_pool = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    if include_punct:
        char_pool += list(string.punctuation)
    char_pool = [ch for ch in char_pool if ch not in disallowed_chars]
    if not char_pool:
        raise ValueError("Character pool is empty after filtering disallowed characters.")
    return "".join(random.choice(char_pool) for _ in range(length))

def write_password_to_file(password, password_type):
    directory = 'Memorable' if password_type.lower() == 'memorable' else 'Random'
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, 'Generated_Passwords.txt')
    current_time = datetime.now().strftime('%A, %B %d, %Y %H:%M:%S')
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"Password: {password} | Created: {current_time}\n")

def main():
    for _ in range(1000):
        chosen_type = random.choice(['memorable', 'random'])
        if chosen_type == 'memorable':
            password = generate_memorable_password(num_words=random.randint(3, 5), case=random.choice(['lower','upper','mixed']))
        else:
            password = generate_random_password(
                length=random.randint(8, 16),
                include_punct=random.choice([True, False]),
                disallowed_chars=[random.choice(string.punctuation)] if random.choice([True, False]) else []
            )
        write_password_to_file(password, chosen_type)

if __name__ == "__main__":
    main()