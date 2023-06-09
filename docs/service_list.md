# List of AWS Services
- `Athena` supports query federation, which enables Athena to query data in the data lake, as well as data stored in other engines such as Amazon Redshift or an Amazon RDS database.
  - `Athena Federated Query`, a feature of Athena, enables you to build connectors so that Athena can query other data sources, beyond just the data in an S3 data lake.
- `Glue` is fully managed ETL (extract, transform, and load) AWS service to analyze and categorize data. 
  - In an ETL pipeline, transformations are performed outside the data warehouse using custom scripts, a cloud-native ETL service such as AWS Glue, or a specialized ETL tool from a commercial vendor such as Informatica, Talend, DataStage, Microsoft, or Pentaho. 
  - **Glue Studio**, a service that provides a visual interface to developing Apache Spark transformations
  - Glue includes a number of components as follows:
    - `Serverless Apache Spark` or `Python shell` environment for performing ETL transformations
    - `Glue Data Catalog`, which provides a centralized logical representation (database and tables) of the data in an Amazon S3 data lake
    - `Glue crawlers` which can be configured to examine files in a specific location, automatically infer the schema of the file, and a
- `Redshift` cloud data warehousing similar to  Snowflake, Google BigQuery, and Azure Synapse
- `Redshift Spectrum` enables a user to write a single query that queries data that has been loaded into the data warehouse, as well as data that exists outside the data warehouse, in the data lake
  - To enable this, the data engineer can configure the Redshift cluster to connect with the AWS Glue Data Catalog, where all the databases and tables for our data lake are defined.
- `Amazon S3` cloud object stores
  - Can store hundreds of petabytes of data at a fraction of the cost of on-premises storage, and they support storing data regardless of its source, format, or structure.
  - Also provide native integrations with hundreds of cloud-native and third-party data processing and analytics tools. 
  - Enabled organizations to build a new, more integrated analytics data management approach, called the **data lake architecture**
- **Data lakehouse** (lake house architecture) approach: `Redshift Spectrum` and `Lake Formation` on AWS, Synapse on Microsoft Azure cloud, and Databricks Delta Lake, is geared to natively integrate the best capabilities of *data lakes and data warehousing*, including the following: 
  - Ability to quickly ingest any type of data:
    -  `Amazon Database Migration Services` (DMS) for ingesting from various databases
    -  `Amazon Kinesis Firehose` to ingest streaming data into the data lake.
  - Storing and processing petabytes of unstructured, semi-structured, and structured data
  - Support for ACID transactions (the ability to concurrently read, insert, update, and delete records in a dataset managed by the data lakehouse)
  - Low latency data access
  - Ability to consume data with a variety of tools, including SQL, Spark, machine learning frameworks, and business intelligence tools
- `Database Migration Service (Amazon DMS)` is a versatile tool that can be used to migrate existing database systems to a new database engine, such as migrating an existing Oracle database to an Amazon Aurora with PostgreSQL compatibility database. But from an analytics perspective, Amazon DMS can also be used to run continuous replication from a number of common database engines into an Amazon S3 data lake.

