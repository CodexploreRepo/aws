# Daily Knowledge

## Day 3

### Glue

- **Glue Job Bookmark** tracks data that has already been processed during a previous run of an ETL job by persisting state information from the job run.
  - Job bookmarks is composed of the **states** for various elements of jobs, such as sources, transformations, and targets.
    - For e.g, an ETL job might read new partitions in an S3 file. Glue tracks which partition the job has processed successfully to prevent duplicate processing and duplicate data in the job’s target data store.
- **Exit a Glue job gracefully**: Since I use bookmarks, sometimes the Glue job can start without having new data to process, the read dataframe is then empty. In this case, I want to end my job properly because it has nothing to do

```Python
job.commit() # Only necessary if you are loading data from s3 and you have job bookmarks enabled.
os._exit(0) # Using a 0 status code throws no exception so your job completes with a succeeded status.
```

- In order to print in Glue console, need to get `logger` of Glue Context

```Python
# set custom logging on
logger = glueContext.get_logger()
```

## Day 2

### Hive, MapReduce, and Apache Spark

- **Apache Hive** provides a SQL-type interface for working with large datasets
- **MapReduce** provides a code-based approach to processing large datasets.
- **Hadoop MapReduce vs Apache Spark**: the biggest difference being that _Apache Spark does all processing in memory_. Apache MapReduce on the other hand _makes extensive use of traditional disk-based reads and writes_ to interim storage during processing.

### Kafka

- Amazon Kinesis and Amazon MSK are services from AWS that offer pub-sub message processing. That is, producers create messages that are written to the streaming service (Kinesis or MSK), and consumers subscribe to receive messages from the service. This is commonly used as a way to decouple applications producing streaming data from applications that are consuming data. Both services can scale up to handle millions of messages per second.
  Kinesis Data Firehose (serverless) automatically scales up and down in response to message throughput changes without requiring any configuration.
- **Amazon Kinesis** is a serverless service, meaning that you never need to make decisions about, manage, or know anything about the underlying servers that run the service. For example, Kinesis Data Firehose automatically scales up and down in response to message throughput changes without requiring any configuration.
  - Much quicker and easier to set up and configure
  - Amazon Kinesis is proprietary software created by AWS, although there are some limited open source elements, such as the Kinesis Agent.
  - Kinesis provides strong integration with several AWS services, such as Amazon S3, Amazon Redshift, and Amazon Elasticsearch. Also provides integration with a limited set of external services such as Splunk and DataDog through **Amazon Kinesis Data Firehose**.
  - While both Amazon Kinesis and Apache Kafka can be used to process a variety of data types. Apache Kafka is most closely compared to Amazon **Kinesis Data Streams** as both provide a powerful way to consume streaming messages.
  - Amazon Kinesis does include several distinct sub-services for specialized use cases.
    - If your use case involves ingesting streaming audio or video data, then Amazon **Kinesis Video Streams** is custom-designed to simplify this type of processing
    - If you want to write out ingested streaming data to targets such as Amazon S3, Amazon Elasticsearch, or Amazon Redshift (as well as some third-party services), then Amazon Kinesis Data Firehose makes this task simple.
- **Amazon MSK** (a managed version of Apache Kafka) is a managed service, meaning AWS manages the infrastructure for you, but you still need to be aware of and make decisions about the underlying compute infrastructure and software such as selecting from a list of instance types to power your MSK cluster, configuring VPC network settings, and also fine-tuning a range of Kafka configuration settings. You also need to select the version of Kafka that you want to use with the service.
  - Provides a lot more options for configuring and fine-tuning the underlying software.
  - Since open-source, there is a large community of contributors to the software, and a large ecosystem providing a diverse range of connectors and integrations. Kafka provides out-of-the-box integration with hundreds of event sources and event sinks (including AWS services such as Amazon S3, but also many other popular products, such as PostgreSQL, Elasticsearch, and others).

### Data Type

#### Parquet

- [Parquet](https://www.linkedin.com/pulse/all-you-need-know-parquet-file-structure-depth-rohan-karanjawala/) file format consists of 2 parts:
  - Data
  - Metadata

### S3

- Bucket name convention: `s3://<company>-<raw/clean/enriched>-<awsregion>-<awsaccountID>-<env>/source/source_region/table_name`
  - `env` dev, test, prod

## Day 1

### Managing Identity and Permissions

Two primary ways to manage which identities can access which resources:

1. `AWS Identity and Access Management (IAM`) service
2. `AWS Lake Formation` to manage data lake access
   <br>

- **Federation of identities** meaning that you can configure IAM to use another identity provider for authentication, such as Active Directory or Okta.
- `IAM identities`
  - **AWS account root user**: strongly recommended that you do not use this identity to log in and perform everyday tasks, but rather create an IAM user for everyday use.
  - **IAM User**: This is an identity that you create and can be used to log in to the AWS Console, run CLI commands, or make API calls.
    - The recommended method to provide access to AWS resources is to make the user part of a group that has relevant IAM policies attached.
  - **IAM User Groups**: You provide permissions (via IAM policies) to an IAM group, and all the members of that group then inherit those permissions.
  - **IAM Role**:
    - used to provide permissions to AWS resources (for example, to provide permissions to an AWS Lambda function so that the Lambda function can access specific AWS resources).
    - used in identity federation, where a user is authenticated by an external system, and that user identity is then associated with an IAM role.

### IAM policies

- To grant authorization to access AWS resources, you can attach an **IAM policy** to an IAM user, IAM group, or IAM role.
- Three types of **identity-based policies** that can be utilized:
  - **AWS managed policies**: these are policies that are created and managed by AWS and provide permissions for common use cases.
    - For example, the `AdministratorAccess` managed policy provides full access to every service and resource in AWS
  - **Customer-managed policies**: these are policies that you create and manage to provide more precise control over your AWS resources.
  - **Inline policies**: These are policies that are written directly for a specific user, group, or role.
- Tips:
  - The recommended method to provide access to AWS resources is to make the user part of `a group` that has relevant IAM policies attached.
  - To make managing large S3-based data lakes easier, AWS introduced a new service called AWS Lake Formation, which enables permissions for the data lake to be controlled by the data lake administrator from within the AWS Management Console

### Data Encryption

- **AWS Key Management Service (KMS)** is to create and manage security keys for encrypting and decrypting data in AWS.
  - For example, in Amazon S3, you can enable **Amazon S3 Bucket Keys**, which configures an S3 Bucket Key to encrypt all new objects in the bucket with an AWS KMS Key.
- **AWS CloudTrail** is to log all use of AWS KMS keys.

### Data Catalog

- 2 types of data catalogs: business catalogs and technical catalogs
- Within AWS, there are two services for interacting with the data catalog: `AWS Glue service`, `AWS Lake Formation`

### Data Lakehouse

- **Data LakeHouse** store the data in S3 (data lake) and use Redshift Serverless as a processing platform along with Redshift Spectrum instead of maintaining Redshift Cluster as a Data Warehouse since maintaining Redshift Cluster is quite expensive

### Concepts

- **Authentication** is the process of validating that a claimed identity is that identity.
- **Authorization** is the process of authorizing access to a resource based on a validated identity.
- **Data security** dictates how an organization should protect data to ensure that data is stored securely (such as in an encrypted state) and that access by unauthorized entities is prevented.
- **Data governance** is related to ensuring that only people that need access to specific datasets to perform their job is granted the access.
  - Governance also applies to ensuring that an organization only uses and processes data on individuals in approved ways and that organizations provide data disclosures as required by law.
