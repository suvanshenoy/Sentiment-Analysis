import string
from collections import Counter

import GetOldTweets3 as got
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def get_tweets(query, since, until, max_tweets):
    tweetCriteria = (
        got.manager.TweetCriteria()
        .setQuerySearch(query)
        .setSince(since)
        .setUntil(until)
        .setMaxTweets(max_tweets)
    )
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    return [tweet.text for tweet in tweets]


def read_and_clean_tweets(tweets):
    text = " ".join(tweets).lower()
    return text.translate(str.maketrans("", "", string.punctuation))


def tokenize_and_remove_stopwords(text):
    tokenized_words = word_tokenize(text, "english")
    return [word for word in tokenized_words if word not in stopwords.words("english")]


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
    fig, ax1 = plt.subplots()
    ax1.bar(emotion_counts.keys(), emotion_counts.values())
    fig.autofmt_xdate()
    plt.savefig(output_path)
    # plt.show()


if __name__ == "__main__":
    tweets = get_tweets("CoronaOutbreak", "2020-01-01", "2020-04-01", 1000)
    text = read_and_clean_tweets(tweets)
    final_words = tokenize_and_remove_stopwords(text)
    emotion_words = read_emotion_words("./data/emotions.txt")
    emotion_counts = get_emotions(final_words, emotion_words)

    print(emotion_counts)
    plot_emotions(emotion_counts, "./visuals/twitter_graph.png")
