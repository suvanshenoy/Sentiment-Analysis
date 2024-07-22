import os
import string
import sys
from collections import Counter

import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import settings
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk_libs = ["punkt", "stopwords", "wordnet", "vader_lexicon"]
settings.download_nltk_lib(nltk_libs)


def read_and_clean_text(file_path):
    try:
        with open(file_path, encoding="utf-8") as file:
            text = file.read().lower()
            return text.translate(str.maketrans("", "", string.punctuation))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""


def tokenize_and_remove_stopwords(text):
    tokenized_words = word_tokenize(text, "english")
    return [word for word in tokenized_words if word not in stopwords.words("english")]


def lemmatize_words(words):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words]


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


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score["neg"] > score["pos"]:
        return "Negative Sentiment"
    elif score["neg"] < score["pos"]:
        return "Positive Sentiment"
    else:
        return "Neutral Sentiment"


def plot_emotions(emotion_counts, output_path):
    fig, ax1 = plt.subplots()
    ax1.bar(emotion_counts.keys(), emotion_counts.values())
    fig.autofmt_xdate()
    plt.title("Nltk Analysis");
    plt.savefig(output_path)
    # plt.show()


if __name__ == "__main__":

    text = read_and_clean_text("./data/sample.txt")
    final_words = tokenize_and_remove_stopwords(text)
    lemma_words = lemmatize_words(final_words)
    emotion_words = read_emotion_words("./data/emotions.txt")
    emotion_counts = get_emotions(lemma_words, emotion_words)

    print(emotion_counts)
    sentiment_result = sentiment_analyse(text)
    print(sentiment_result)
    plot_emotions(emotion_counts, "./visuals/nltk_graph.png")
