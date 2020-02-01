from kafka import KafkaConsumer, KafkaProducer
from workshop.common.ReviewProcessor import get_reviews, predict, train
import argparse
import logging

producer = KafkaProducer(bootstrap_servers='localhost:9092')


def send_review(review, topic='default-review'):
    logging.debug("send_review topic={topic} review={review}".format(topic=topic, review=review))
    # send review.
    producer.send(topic, value=bytes(review, "utf-8"))
    producer.flush()


def consume_reviews(review_handler, topic='default-review', consumer_group='test'):
    logging.debug("consume_reviews topic={topic} consumer_group={consumer_group}".format(topic=topic,
                                                                                         consumer_group=consumer_group))
    count = 0
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092', group_id=consumer_group)
    for record in consumer:
        review = record.value.decode("utf-8")
        logging.info("review={review}".format(review = review))
        if count % 100 == 0:
            logging.info("Consumed count={count} reviews".format(count = count))
        review_handler(review)
        count += 1


if __name__ == '__main__':

    reviews = get_reviews()[:100000]

    parser = argparse.ArgumentParser()

    parser.add_argument("--mode", help="CONSUMER/PRODUCER")
    parser.add_argument("--topic", help="topic of interest")
    parser.add_argument("--consumer_group", help="consumer group")
    parser.add_argument("--task", help="predict/train")
    args = parser.parse_args()
    logging.debug("args mode={mode} topic={topic}".format(mode=args.mode, topic=args.topic))
    topic = args.topic
    if args.mode == "PRODUCER":
        for idx, review in enumerate(reviews):
            if idx % 100 == 0:
                logging.warning("Sent numReviews={count} to topic={topic}".format(count = idx + 1, topic = topic))
            send_review(review, topic)

    elif args.mode == "CONSUMER":

        # TODO Use two different consumer groups for train and predict.
        print("Need to implement for task={task}".format(task = args.task))
        # To ensure that each review is used for predict as well as train.
        pass

