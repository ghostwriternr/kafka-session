# Console Producer and Consumer
## Start Zookeeper
Kafka uses [ZooKeeper](https://zookeeper.apache.org/) so you need to first start a ZooKeeper server if you don't already have one.
```sh
> sh bin/zookeeper-server-start.sh config/zookeeper.properties
```

## Start Kafka Broker
```sh
> sh bin/kafka-server-start.sh config/server.properties
```

## Create a topic
Let's create a topic named "test" with a single partition and only one replica:
1
```sh
> sh bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```

We can now see that topic if we run the list topic command:
```sh
> sh bin/kafka-topics.sh --list --bootstrap-server localhost:9092
test
```
Alternatively, instead of manually creating topics you can also configure your brokers to auto-create topics when a non-existent topic is published to.

## Send messages using the console producer
Kafka comes with a command line client that will take input from a file or from standard input and send it out as messages to the Kafka cluster. By default, each line will be sent as a separate message.

Run the producer and then type a few messages into the console to send to the server.
```sh
> sh bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
This is a message
This is another message
```

## Start a consumer
Kafka also has a command line consumer that will dump out messages to standard output.
```sh
> sh bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
This is a message
This is another message
```

If you have each of the above commands running in a different terminal then you should now be able to type messages into the producer terminal and see them appear in the consumer terminal. 
