from typing import List

import nltk


def download_nltk_lib(nltk_libs: List[str]):
    for nltk_lib in nltk_libs:
        nltk.download(nltk_lib)


nltk_libs = ["punkt", "stopwords", "wordnet", "vader_lexicon"]
download_nltk_lib(nltk_libs)
