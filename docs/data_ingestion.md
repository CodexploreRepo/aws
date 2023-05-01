# AWS services for ingesting data
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
  - `Kinesis Data Firehose`: Ingests streaming data, buffers for a configurable period, then writes out to a limited set of targets (S3, Redshift, Elasticsearch, Splunk, and others)
  - `Kinesis Data Streams`: Ingests real-time data streams, processing the incoming data with a custom application and low latency
  - `Kinesis Data Analytics`: Reads data from a streaming source and uses SQL statements or Apache Flink code to perform analytics on the stream
  - `Kinesis Video Streams`: Processes streaming video or audio streams, as well as other time-serialized data such as thermal imagery and RADAR data

### Amazon Kinesis Agent
- In addition to the AWS Kinesis services, AWS also provides an agent to easily consume data from a file and write that data out in a stream to either Kinesis Data Streams or Kinesis Data Firehose.
- The agent can be configured to monitor a set of files, and as new data is written to the file, the agent buffers the data (configurable for a duration of between 1 second and 15 minutes) and then writes the data to Kinesis. The agent handles retry on failure, as well as file rotation and checkpointing.
- For example: The Kinesis Agent can be configured to monitor the Apache web server log files on your web server, convert each record from the Apache access log format to JSON format, and then write records out reflecting all website activity every 30 seconds to Kinesis, where Kinesis Data Analytics can be used to analyze events and generate custom metrics based on a tumbling 5-minute window.

#### When to use & not to use Amazon Kinesis Agent
- **When to use**: The Amazon Kinesis Agent is ideal for when you want to stream data to Kinesis that is being written to a file in a separate process (such as log files).
- **When not to use**: If you have a custom application where you want to emit streaming events (such as a mobile application, or IoT device) you may want to consider using the `Amazon Kinesis Producer Library (KPL)`, or the `AWS SDK`, to integrate sending streaming data directly with your application.
