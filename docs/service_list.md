# List of AWS Services
- **ETL (extract, transform, and load)**: `AWS Glue` is fully managed ETL (extract, transform, and load) AWS service to analyze and categorize data. 
  - In an ETL pipeline, transformations are performed outside the data warehouse using custom scripts, a cloud-native ETL service such as AWS Glue, or a specialized ETL tool from a commercial vendor such as Informatica, Talend, DataStage, Microsoft, or Pentaho. 
  - You can use AWS Glue crawlers to automatically infer database and table schema from your data in Amazon S3 and store the associated metadata in the `AWS Glue Data Catalog`.
  - AWS Glue also provides a **serverless Apache Spark environment**
- **Cloud data warehousing**: `Amazon Redshift`, Snowflake, Google BigQuery, and Azure Synapse
- **Cloud object stores**: `Amazon S3`
  - Can store hundreds of petabytes of data at a fraction of the cost of on-premises storage, and they support storing data regardless of its source, format, or structure.
  - Also provide native integrations with hundreds of cloud-native and third-party data processing and analytics tools. 
  - Enabled organizations to build a new, more integrated analytics data management approach, called the **data lake architecture**
- **Data lakehouse** (lake house architecture) approach:  `Redshift Spectrum` and `Lake Formation` on AWS, Synapse on Microsoft Azure cloud, and Databricks Delta Lake, is geared to natively integrate the best capabilities of *data lakes and data warehousing*, including the following: 
  - Ability to quickly ingest any type of data:
    -  `Amazon Database Migration Services` (DMS) for ingesting from various databases
    -  `Amazon Kinesis Firehose` to ingest streaming data into the data lake.
  - Storing and processing petabytes of unstructured, semi-structured, and structured data
  - Support for ACID transactions (the ability to concurrently read, insert, update, and delete records in a dataset managed by the data lakehouse)
  - Low latency data access
  - Ability to consume data with a variety of tools, including SQL, Spark, machine learning frameworks, and business intelligence tools
- **Database Migration Service (Amazon DMS)** is a versatile tool that can be used to migrate existing database systems to a new database engine, such as migrating an existing Oracle database to an Amazon Aurora with PostgreSQL compatibility database. But from an analytics perspective, Amazon DMS can also be used to run continuous replication from a number of common database engines into an Amazon S3 data lake.

