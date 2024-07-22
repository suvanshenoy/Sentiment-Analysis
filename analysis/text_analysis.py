import os
import string
from collections import Counter

import matplotlib.pyplot as plt


def read_and_clean_text(file_path):
    try:
        with open(file_path, encoding="utf-8") as file:
            text = file.read().lower()
            return text.translate(str.maketrans("", "", string.punctuation))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""


def tokenize_and_remove_stopwords(text, stop_words):
    tokenized_words = text.split()
    return [word for word in tokenized_words if word not in stop_words]


def read_emotion_words(file_path):
    emotion_list = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                clear_line = (
                    line.replace("\n", "").replace(",", "").replace("'", "").strip()
                )
                word, emotion = clear_line.split(":")
                emotion_list.append((word, emotion))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return emotion_list


def get_emotions(final_words, emotion_words):
    emotion_list = [emotion for word, emotion in emotion_words if word in final_words]
    return Counter(emotion_list)


def plot_emotions(emotion_counts, output_path):
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    fig, ax1 = plt.subplots()
    ax1.bar(emotion_counts.keys(), emotion_counts.values())
    fig.autofmt_xdate()
    plt.title("Text Analysis");
    plt.savefig(output_path)
    # plt.show()  # Commented out to avoid the warning


if __name__ == "__main__":
    stop_words = [
        "i",
        "me",
        "my",
        "myself",
        "we",
        "our",
        "ours",
        "ourselves",
        "you",
        "your",
        "yours",
        "yourself",
        "yourselves",
        "he",
        "him",
        "his",
        "himself",
        "she",
        "her",
        "hers",
        "herself",
        "it",
        "its",
        "itself",
        "they",
        "them",
        "their",
        "theirs",
        "themselves",
        "what",
        "which",
        "who",
        "whom",
        "this",
        "that",
        "these",
        "those",
        "am",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "having",
        "do",
        "does",
        "did",
        "doing",
        "a",
        "an",
        "the",
        "and",
        "but",
        "if",
        "or",
        "because",
        "as",
        "until",
        "while",
        "of",
        "at",
        "by",
        "for",
        "with",
        "about",
        "against",
        "between",
        "into",
        "through",
        "during",
        "before",
        "after",
        "above",
        "below",
        "to",
        "from",
        "up",
        "down",
        "in",
        "out",
        "on",
        "off",
        "over",
        "under",
        "again",
        "further",
        "then",
        "once",
        "here",
        "there",
        "when",
        "where",
        "why",
        "how",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "no",
        "nor",
        "not",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "can",
        "will",
        "just",
        "don",
        "should",
        "now",
    ]

    text = read_and_clean_text("../data/sample.txt")
    final_words = tokenize_and_remove_stopwords(text, stop_words)
    emotion_words = read_emotion_words("../data/emotions.txt")
    emotion_counts = get_emotions(final_words, emotion_words)

    print(emotion_counts)
    plot_emotions(emotion_counts, "../visuals/graph.png")
