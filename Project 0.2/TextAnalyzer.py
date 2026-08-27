# Project 0.2: Python Fundamentals - Text Analyzer

def extract_text(filename: str) -> str:
    with open(filename, 'r') as file:
        text = file.readlines()
    return text

def remove_punctuations(text: str) -> tuple[str, list]:
    punctuations = [".", "?", "!", ",", ":", ";", "-", "--", "(", ")", "[", "]", "{", "}", "'", '"']
    new_text = text
    for punctuation in punctuations:
        new_text.replace(punctuation, "")
    words = new_text.replace('\n', ' ').lower().split()
    return new_text, words


def extract_data(arr_of_txt: list[str]) -> tuple:
    paragraph = ' '.join(arr_of_txt)
    words = paragraph.replace('\n', ' ').lower().split()
    special_chars = 0
    sentence_count = 0
    words_count = len(words)

    for i in paragraph:
        if not i.isalnum() and not i.isspace():
            special_chars += 1
            if i in [".", "?", "!", ";"]:
                sentence_count += 1

    paragraph, words = remove_punctuations(paragraph)

    counter = {}
    for word in words:
        if word in counter:
             counter[word] += 1
        else:
            counter[word] = 1
    max_freq = max(counter.values())
    most_common_words = [max_num for max_num in counter if counter[max_num] == max_freq]

    return most_common_words, words_count, sentence_count, special_chars

arr = extract_text("example.txt")
data = extract_data(arr)
print(data)