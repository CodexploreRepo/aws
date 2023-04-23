# Data Warehouse with Amazon Redshift
- `Amazon Redshift` is a modern cloud-native data warehouses, leverage parallel processing and columnar storage to store and process petabytes of data. Amazon Redshift provides very high query throughput while processing high data volumes.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/233819130-5bb29995-7694-4935-b99c-c1f28b340aa2.png"
</p>
  
- At the center of our architecture is the enterprise data warehouse, which hosts a set of data assets that contain current and historical data about key business subject areas. 
- On the left-hand side, we have our source systems and an ETL pipeline to load the data into the warehouse. 
- On the right-hand side, we can see several systems/applications that consume data from the data warehouse.
  
## ETL
- In an ETL pipeline, transformations are performed outside the data warehouse using custom scripts, a cloud-native ETL service such as AWS Glue, or a specialized ETL tool from a commercial vendor such as Informatica, Talend, DataStage, Microsoft, or Pentaho.

## Data Lakehouse 
### Data Lakehouse Implemenetations
- Over the last 2 to 3 years, various cloud providers, software providers, and open source organizations have been building new products to enable this move toward a **data lakehouse architecture**.
- The implementation approaches to a data lakehouse (also sometimes referred to as data lakehouse) vary across different platform providers:
  - `Databricks` has introduced an offering called Databricks Delta Lake. Delta Lake provides a storage layer that enables ACID transactions directly in the data lake. With this functionality, records can be inserted, updated, and deleted for tables in the data lake, something that was previously not easily available.
  - `Apache Hudi` is a relatively new open source project that enables users to perform insert, update, and delete operations on data in the data lake, without needing to build their own custom solutions.
  - `Microsoft Azure` has added a capability called Polybase to their warehouse service, known as Azure Synapse Analytics. Polybase allows Azure Synapse Analytics users to include data stored in Azure Blob storage, Azure Data Lake Store, and Hadoop to help process their T-SQL queries.
  - `Amazon Web Services (AWS)` has added several new capabilities, including new features in Redshift Spectrum and Lake Formation, to enable building a data lakehouse architecture on AWS. This includes the ability to read data lake tables in S3 from Amazon Redshift, as well as to perform inserts, updates, and deletes on data lake tables using Lake Formation governed tables.  

 ### Building a data lakehouse on AWS
- Two main components that provide the key foundations for building a lake house architecture in AWS are 
  - `Amazon Redshift Spectrum` a feature of the Amazon Redshift data warehouse service that enables Redshift to read data stored in S3. 
    - a query processing layer that uses Amazon-managed compute nodes to natively query structured and semi-structured data hosted in data lake storage (S3). 
    - Spectrum enables an Amazon Redshift data warehouse to present a single unified interface, where users can run SQL statements that combine data from both Redshift (data warehouse) and S3 (data lake). 
    - Spectrum thus enables users to query all the data in the lake house using a single SQL interface.
  - `AWS Lake Formation` provides the **central lake house catalog** where users and analytics services can search, discover, and retrieve metadata for a dataset by using the catalog automation capability provided by AWS Glue.
    - Glue can be configured to periodically crawl through the lake house storage and discover datasets, extract their metadata (such as location, schema, format, partition information, and more), and then store this metadata as a table in the central Lake Formation catalog. 
    - The metadata of a table in the catalog can be used by AWS analytics services, such as Amazon Athena, to locate a corresponding dataset in the lake house storage and apply schema-on-read to that dataset during query execution.
    - AWS has also enhanced the AWS Lake Formation service to support governed tables.
- Processing and consumption layers to be able to access all lake house data
  - `Redshift SQL` 
  - `Apache Spark interface` for example
    - AWS Glue (which provides a serverless Apache Spark environment)
    - Amazon EMR (a managed Spark environment) include native Spark plugins that can access Redshift tables, in addition to objects in S3 buckets, all in the same job. 
  - `Amazon Athena` supports query federation, which enables Athena to query data in the data lake, as well as data stored in other engines such as Amazon Redshift or an Amazon RDS database.

<p align="center"><img width=700 src="https://user-images.githubusercontent.com/64508435/233845970-bc46c6ad-0919-4fad-bef8-9f48ee0e8326.png"
</p>  
