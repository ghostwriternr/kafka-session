from kafka import KafkaConsumer, KafkaProducer
from workshop.common.ReviewProcessor import get_reviews, predict, train
import argparse
import logging


def send_review(review, topic='default-review'):
    logging.info("send_review topic={topic} review={review}".format(topic=topic, review=review))

    # send review.

    # create producer [global / local] with bootstrap servers at localhost:9092

    # produce and flush the message.


def consume_reviews(review_handler, topic='default-review', consumer_group='test'):
    logging.info("consume_reviews topic={topic} consumer_group={consumer_group}".format(topic=topic,
                                                                                        consumer_group=consumer_group))
    count = 0

    # create kafka consumer at localhost:9092

    consumer = None

    for record in consumer:

        review = record.value.decode("utf-8")

        logging.info("review={review}".format(review=review))

        if count % 100 == 0:

            logging.info("Consumed count={count} reviews".format(count=count))

        review_handler(review)

        count += 1


if __name__ == '__main__':

    reviews = get_reviews()[:10000]

    parser = argparse.ArgumentParser()

    parser.add_argument("--mode", help="CONSUMER/PRODUCER")
    parser.add_argument("--topic", help="topic of interest")
    parser.add_argument("--consumer_group", help="consumer group")
    args = parser.parse_args()
    logging.debug("args mode={mode} topic={topic}".format(mode=args.mode, topic=args.topic))
    topic = args.topic
    if args.mode == "PRODUCER":
        for idx, review in enumerate(reviews):
            send_review(review, topic)
            if idx % 100 == 0:
                logging.info("Sent numReviews={count} to topic={topic}".format(count=idx + 1, topic=topic))

    elif args.mode == "CONSUMER":
        consume_reviews(predict, topic, args.consumer_group)

