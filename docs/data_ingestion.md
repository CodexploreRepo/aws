# AWS Services for Transforming Data
The first step in building big data analytic solutions is to ingest data from a variety of sources into AWS

## Amazon Database Migration Service (DMS)
- One of the most common ingestion use cases is to sync data from a traditional database system into an analytic pipeline, either landing the data in 
  - an Amazon S3-based data lake
  - a data warehousing system such as Amazon Redshift.
- `Amazon DMS` is a versatile tool that can be used to migrate existing database systems to a new database engine, such as migrating an existing Oracle database to an Amazon Aurora with PostgreSQL compatibility database. 
- But from an analytics perspective, Amazon DMS can also be used to run continuous replication from a number of common database engines into an Amazon S3 data lake.
### When to use & not to use Amazon DMS
- **When to use**: Amazon DMS simplifies migrating from one database engine to a different database engine, or syncing data from an existing database to Amazon S3 on an ongoing basis.
- **When not to use**: If you're looking to sync an on-premises database to the same engine in AWS, it is often better to use native tools from that database engine. DMS is primarily designed for heterogeneous migrations (that is, from one database engine to a different database engine).
### How Amazon DMS works
- do an initial load of data from the databases into S3, specifying the format that we want the file written out in (CSV or Parquet), and the specific ingestion location in S3.
- At the same time, we can also set up a DMS task to do ongoing replication from the source databases into S3 once the full load completes
- With transactional databases, the rows in a table are regularly updated, such as if a customer changes their address or telephone number. 
- DMS uses the **database transaction log files** from the database to track updates to rows in the database and writes out the target file in S3 with an extra column added (`Op`) that indicates which operation is reflected in the row – an insert, update, or deletion.
  - The process of tracking and recording these changes is commonly referred to as **Change Data Capture (CDC)**. 
  - For example: a source table with a schema of `custid`, `lastname`, `firstname`, `address`, and `phone`, and the following sequence of events happens:
    - A new customer is added with all fields completed.
    - The phone number was entered incorrectly, so the record has the phone number updated.
    - The customer record is then deleted from the database.
    ```Python
    # CDC file that was written out by DMS
    I, 9335, Smith, John, "1 Skyline Drive, NY, NY", 201-555-9012 # a new record was inserted into the table (represented by the I in the first column).
    U, 9335, Smith, John, "1 Skyline Drive, NY, NY", 201-555-9034 # a record was updated (represented by the U in the first column)
    D, 9335, Smith, John, "1 Skyline Drive, NY, NY", 201-555-9034 # this record was deleted from the table (represented by the D in the first column)
    ```
## Amazon Kinesis for Streaming Data Ingestion
- Amazon Kinesis is a managed service that simplifies the process of ingesting and processing streaming data in real time, or near real time.
### Amazon Kinesis services
  - `Kinesis Data Firehose`: Ingests  data in near real time from streaming sources, buffers for a configurable period, then writes out to a limited set of Amazon targets (S3, Redshift, Elasticsearch) as well as third-party services (such as Splunk, Datadog, and New Relic).
  - `Kinesis Data Streams`: Ingests real-time data streams, processing the incoming data with a custom application and low latency
  - `Kinesis Data Analytics`: Reads data from a streaming source and uses SQL statements or Apache Flink code to perform analytics on the stream
  - `Kinesis Video Streams`: Processes streaming video or audio streams, as well as other time-serialized data such as thermal imagery and RADAR data
#### Kinesis Data Firehose
- A common use case for data engineering purposes is to ingest website clickstream data from the Apache web logs on a web server and write that data out to an S3 data lake (or a Redshift data warehouse).
- In this example, you could install the Kinesis Agent on the web server and configure it to monitor the Apache web server log files.
- **When to use**: Amazon Kinesis Firehose is the ideal choice for when you want to receive streaming data, buffer that data for a period, and then write the data to one of the targets supported by Kinesis Firehose (such as Amazon S3, Amazon Redshift, Amazon Elasticsearch, or a supported third-party service).
- **When not to use**: If your use case requires very low latency processing of incoming streaming data (that is, immediate reading of received records), or you want to use a custom application to process your incoming records or deliver records to a service not supported by Amazon Kinesis Firehose, then you may want to consider using `Amazon Kinesis Data Streams` or `Amazon Managed Streaming for Apache Kafka (MSK)` instead.

#### Kinesis Data Streams
- Kinesis Data Streams provides increased flexibility for how data is consumed and makes the incoming data available to your streaming applications with very low latency 
- You can write to Kinesis Data Streams using the Kinesis Agent, or you can develop your own custom applications using the AWS SDK or the KPL, a library that simplifies writing data records with high throughput to a Kinesis data stream.
- **When to use**: Amazon Kinesis Data Streams is ideal for use cases where you want to process incoming data as it is received, or you want to create a high-availability cluster of servers to process incoming data with a custom application.
- **When not to use**: If you have a simple use case that requires you to write data to specific services in near real time, you should consider Kinesis Firehose if it supports your target destination. If you are looking to migrate an existing Apache Kafka cluster to AWS, then you may want to consider migrating to Amazon MSK. If Apache Kafka supports third-party integration that would be useful to you, you may want to consider Amazon MSK.

#### Amazon Kinesis Data Analytics
- Amazon Kinesis Data Analytics simplifies the process of processing streaming data, using either standard SQL queries or an Apache Flink application.
- An example of a use case for Kinesis Data Analytics is to analyze incoming clickstream data from an e-commerce website to get near real-time insight into the sales of a product. 
  - This enables the business to quickly get answers to questions such as "how many sales of product x have there been in each 5-minute period since our promotion went live?"
- **When to use**: If you want to use SQL expressions to analyze data or extract key metrics over a rolling time period, Kinesis Data Analytics significantly simplifies this task. If you have an existing Apache Flink application that you want to migrate to the cloud, consider running the application using Kinesis Data Analytics. 
### Amazon Kinesis Agent
- In addition to the AWS Kinesis services, AWS also provides an agent to easily consume data from a file and write that data out in a stream to either Kinesis Data Streams or Kinesis Data Firehose.
- The agent can be configured to monitor a set of files, and as new data is written to the file, the agent buffers the data (configurable for a duration of between 1 second and 15 minutes) and then writes the data to Kinesis. The agent handles retry on failure, as well as file rotation and checkpointing.
- For example: The Kinesis Agent can be configured to monitor the Apache web server log files on your web server, convert each record from the Apache access log format to JSON format, and then write records out reflecting all website activity every 30 seconds to Kinesis, where Kinesis Data Analytics can be used to analyze events and generate custom metrics based on a tumbling 5-minute window.

#### When to use & not to use Amazon Kinesis Agent
- **When to use**: The Amazon Kinesis Agent is ideal for when you want to stream data to Kinesis that is being written to a file in a separate process (such as log files).
- **When not to use**: If you have a custom application where you want to emit streaming events (such as a mobile application, or IoT device) you may want to consider using the `Amazon Kinesis Producer Library (KPL)`, or the `AWS SDK`, to integrate sending streaming data directly with your application.

## Amazon MSK for Streaming Data Ingestion
- Apache Kafka is a popular open source distributed event streaming platform that enables an organization to create high-performance streaming data pipelines and applications, and Amazon MSK (Managed Streaming for Apache Kafka) is a managed version of Apache Kafka available from AWS.
- While Apache Kafka is a popular choice for organizations, it can be a challenge to install, scale, update, and manage in an on-premises environment, often requiring specialized skills. 
- To simplify these tasks, AWS offers Amazon MSK, which enables an organization to deploy an Apache Kafka cluster with a few clicks in the console, and reduces the management overhead by automatically monitoring cluster health and replacing failed components.

### When to use & not to use Amazon MSK
- **When to use**: Amazon MSK is an ideal choice if your use case is a replacement for an existing Apache Kafka cluster, or if you want to take advantage of the many third-party integrations from the open source Apache Kafka ecosystem.
- **When not to use**: Amazon Kinesis may be a better streaming solution if you are creating a new solution from scratch, as Kinesis is serverless and you only pay for data throughput (whereas with Amazon MSK you pay for the cluster, whether you are sending data through it or not).
