import pickle
import logging
from gensim.models import Word2Vec
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

PROJECT_DIR = "/Users/nramesh/dev/kafka-session"
# Tokenizer to remove non-alphabets in words.
alpha_regex_tokenizer = tokenize.RegexpTokenizer(r'\w+')

# Vader based sentiment analyzer
sid = SentimentIntensityAnalyzer()

# All reviews seen until now.
overall_reviews = []


def predict(review):
    logging.debug("Predicting review..")
    sentences = clean(review)
    overall_scores = []
    for sentence in sentences:
        logging.debug("Predicting sentiment for {sentence}".format(sentence=sentence))
        scores = sid.polarity_scores(sentence)
        overall_scores.append(scores)
    return overall_scores


def clean(review):
    logging.debug("Cleaning review..")
    tokenized_sentences = tokenize.sent_tokenize(review)
    return [' '.join(alpha_regex_tokenizer.tokenize(sentence)) for sentence in tokenized_sentences]


def train(review):
    cleansed_review_sentences = clean(review)
    logging.debug("Adding review to dataset..")
    overall_reviews.extend(cleansed_review_sentences)

    if len(overall_reviews) % 100 == 0:
        print("Training word2vec with numReviews={length}".format(length=len(overall_reviews)))
        model = Word2Vec(overall_reviews, min_count=1, size=50, workers=3, window=3, sg=1)
        # Saving for reuse.
        model.save("review-word2vec.model")
        logging.debug("Completed training..")


def get_reviews():
    with open(PROJECT_DIR + "/data/dataset.pkl", "rb") as dataset_file:
        reviews = pickle.load(dataset_file)
    return reviews


if __name__ == '__main__':

    reviews = get_reviews()[:1000]

    for review in reviews:
        predict(review)

    print("Done with prediction..", len(reviews))

    for idx, review in enumerate(reviews):
        train(review)

    print("Done with training..", len(reviews))
