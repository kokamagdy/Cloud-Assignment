import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter


nltk.download("punkt")
nltk.download("stopwords")


file_path = "random_paragraphs.txt"


def remove_stopwords_from_text(file_path):

    with open(file_path, "r") as file:
        text = file.read()

    words = word_tokenize(text)

    stop_words = set(stopwords.words("english"))

    filtered_words = [word for word in words if word.lower() not in stop_words]

    filtered_text = " ".join(filtered_words)

    return filtered_text


result_text = remove_stopwords_from_text(file_path)
print("Text after removing stop words:")
print(result_text)


def count_word_frequency(file_path):

    with open(file_path, "r") as file:
        text = file.read()

    words = word_tokenize(text)

    words = [word.lower() for word in words if word.isalnum()]

    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    word_freq = Counter(words)

    return word_freq


word_frequencies = count_word_frequency(file_path)

for word, frequency in word_frequencies.items():
    print(f"Word: {word} , Frequency: {frequency}")
