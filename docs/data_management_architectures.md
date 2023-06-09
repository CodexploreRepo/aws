# Data Management Architectures for Analytics

## Data Warehouse with Amazon Redshift
- `Amazon Redshift` is a modern cloud-native data warehouses, leverage parallel processing and columnar storage to store and process petabytes of data. Amazon Redshift provides very high query throughput while processing high data volumes.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/233819130-5bb29995-7694-4935-b99c-c1f28b340aa2.png"><br>Enterprise data warehousing architecture</p>
  
- At the center of our architecture is the enterprise data warehouse, which hosts a set of data assets that contain current and historical data about key business subject areas. 
- On the left-hand side, we have our source systems and an ETL pipeline to load the data into the warehouse. 
- On the right-hand side, we can see several systems/applications that consume data from the data warehouse.
### Amazon Redshift cluster
Amazon Redshift cluster contains several compute resources, along with their associated disk storage. There are two types of nodes in a Redshift cluster:
- **One leader node**, which interfaces with client applications, receives and parses queries, and coordinates query execution on compute nodes
- **Multiple compute nodes**, which store warehouse data and run query execution steps in parallel.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/233854168-82a7e899-6066-4283-a596-72e8aa3cd4ae.png"><br>Massively Parallel Processing (MPP) architecture of an Amazon Redshift cluster</p>

### SQL queries in Redshift cluster
- User connects to the Redshift leader node (via JDBC or ODBC). This node does not query data directly but is effectively the central brain behind all the queries that do run on the cluster. 
- We will demo with below example: In a modern analytic environment, a common use case for a data warehouse would be to load a subset of data from the data lake into the warehouse, based on which data needs to be queried most frequently and which data needs to be used for queries requiring the best possible performance.
  - Knowing that 80% of the reporting and queries will be on the last 12 months of sales data, the data engineer may also design a process to remove all data that's more than 12 months old from the data warehouse.
  - 20% of queries that need to include historical data that's more than 12 months old? That's where **Redshift Spectrum** comes in, a feature of Amazon Redshift that *enables a user to write a single query that queries data that has been loaded into the data warehouse, as well as data that exists outside the data warehouse, in the data lake*.
    -  To enable this, the data engineer can configure the Redshift cluster to connect with the AWS Glue Data Catalog, where all the databases and tables for our data lake are defined. 
    - Once that has been configured, a user can reference both internal Redshift tables and tables registered in the Glue data catalog.
- Step 1. Using a SQL client, the user makes a connection and authenticates with the Redshift leader node, and sends through a SQL statement that queries 
  - `current_sales` table (a table in which the data exists within the Redshift cluster and contains the past 12 months of sales data)
  - `historical_sales` table (a table that is registered in the Glue data catalog, and where the data files are located in the Amazon S3 data lake, which contains historical sales data going back 10 years).
- Step 2. The leader node analyzes and optimizes the query, compiles a query plan, and pushes individual query execution plans to the compute nodes in the cluster.
- Step 3. The compute nodes query data they have locally (for the `current_sales` table) and query the AWS Glue Data Catalog to gather information on the external `historical_sales` table. Using the information they gathered, they can optimize queries for the external data and push those queries out to the **Redshift Spectrum** layer.
- Step 4. **Redshift Spectrum** is outside of a customer's Redshift cluster and is made up of thousands of worker nodes (Amazon EC2 compute instances) in each AWS Region. These worker nodes are able to scan, filter, and aggregate data from the files in Amazon S3, and then stream results back to the Amazon Redshift cluster.
- Step 5. The **Redshift cluster** performs final operations to join and merge data, and then returns the results to the user's SQL client.
<p align="center"><img width=400 src="https://user-images.githubusercontent.com/64508435/236505677-4ab3b080-8f41-497f-9db6-26b5eb700b78.png"><br>Redshift architecture</p>

### Understanding the role of `data marts`
- Data warehouses contain data from all relevant business domains and have a comprehensive but complex schema. 
- A `data mart` is focused on a single business subject repository (for example, marketing, sales, or finance) and is typically created to serve a narrower group of business users, such as a single department. 
- A data mart often has a set of denormalized fact tables organized in a much simpler schema compared to that of an enterprise data warehouse
### Feeding data into the warehouse 
- Feeding data into the warehouse – ETL and ELT pipelines
- The decision as to whether to build an Extract-Transform-Load (ETL) or Extract-Load-Transform (ELT) data pipeline is based on the following:
  - The complexity of the required data transformations.
  - The speed at which source data needs to be made available for analysis in the data warehouse after it's produced in the source system.
#### ETL
- To bring data into the warehouse (and optionally, data marts), organizations typically build data pipelines that do the following:
  - Extract data from various sources and stores it in a staging area first (a system outside the warehouse).
  - Transform source data by validating, cleaning, standardizing, curating and converting it into a form suitable so that it can be loaded into the data warehouse (and optionally, data marts). 
  - Load the transformed source data into the enterprise data warehouse schema, and optionally a data mart as well.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/233854716-a14f3925-0285-48bc-931b-a73e3f2bca9a.png"><br>ETL pipeline</p>

- In an ETL pipeline, transformations are performed outside the data warehouse using custom scripts, a cloud-native ETL service such as AWS Glue, or a specialized ETL tool from a commercial vendor such as Informatica, Talend, DataStage, Microsoft, or Pentaho.
##### When to use ETL ?
An ETL approach to building a data pipeline is typically used when the following are true:
- Source database technologies and formats are different from those of the data warehouse
- Data volumes are small to moderate
- Data transformations are complex and compute-intensive
- 
#### ELT 
- On the other hand, an ELT pipeline extracts data (typically, highly structured data) from various sources and loads it as-is (matching the sources systems' data structures) into a staging area within the data warehouse. 
- The database engine powering the data warehouse is then used to perform transformation operations on the staged data to make it ready for consumption.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/233854974-ee90d91b-0cd7-47be-a49f-be625286ded8.png"><br>ELT pipeline</p>

##### When to use ELT ?
The ELT approach allows for rapidly loading large amounts of source data into the warehouse. Furthermore, the MPP architecture of modern data warehouses can significantly accelerate the transform steps in ELT pipelines. The ELT approach is typically leveraged when the following are true:
- Data sources and the warehouse have similar database technologies, making it easier to directly load source data into the staging tables in the warehouse.
- A large volume of data needs to be quickly loaded into the warehouse.
- All the required transformation steps can be executed using the native SQL capabilities of the warehouse's database engine.

## Data Lake
### Definition
- A cloud data lake is a central, highly scalable repository in the cloud where an organization can manage exabytes of various types of data, such as the following:
  - Structured data (row-column-based tables)
  - Semi-structured data (such as JSON and XML files, log records, and sensor data streams)
  - Unstructured data (such as audio, video streams, Word/PDF documents, and emails)
- Data from any of these sources can be quickly loaded into the data lake as-is (keeping the original source format and structure). Unlike with data warehouses, data does not need to be converted into a standard structure.
- A cloud data lake also natively integrates with cloud analytic services that are decoupled from data lake storage and enables diverse analytic tools, including: 
  - SQL
  - Code-based tools (such as Apache Spark)
  - Specialized machine learning tools
  - Business intelligence visualization tools.

### Data Lake Logical Architecture
<p align="center"><img width=700 src="https://user-images.githubusercontent.com/64508435/233855351-05a9ca05-670c-4cb4-98cf-02a2d1d20fa0.png"><br>Data lake logical layered architecture</p>

#### Storage Layer and Storage Zones
- At the center of the data lake architecture is the `storage layer`, which provides virtually unlimited, low-cost storage that can store a variety of datasets, irrespective of their structure or format.
- The storage layer is organized into different zones, with each zone having a specific purpose:
  - **Landing/raw zone**: This is the zone where the ingestion layer writes data, as-is, from the source systems. The landing/raw zone permanently stores the raw data from source.
  - **Clean/transform zone**: The initial data processing of data in the landing/raw zone, such as validating, cleaning, and optimizing datasets, writes data into the clean/transform zone. The data here is often stored in optimized formats such as Parquet, and it is often partitioned to accelerate query execution and downstream processing. Data in this zone may also have had PII information removed, masked, or replaced with tokens.
  - **Curated/enriched zone**: The data in the clean/transformed zone may be further refined and enriched with business-specific logic and transformations, and this data is written to the curated/enriched zone. This data is in its most consumable state and meets all organization standards (cleanliness, file formats, schema). Data here is typically partitioned, cataloged, and optimized for the consumption layer

#### Cataloging and search layer
- The cataloging and search layer provides this metadata (schema, partitioning information, categorization, ownership, and more) about the datasets hosted in the storage layer. 

#### Ingestion layer
- The ingestion layer is responsible for connecting to diverse types of data sources and bringing their data into the storage layer of the data lake. 

#### Processing layer
- Once the ingestion layer brings data from a source system into the landing zone, it is the processing layer that makes it ready for consumption by data consumers. The processing layer transforms the data in the lake through various stages of data cleanup, standardization, and enrichment.

#### Consumption layer
- Once data has been ingested and processed to make it consumption-ready, it can be analyzed using several techniques, such as interactive query processing, business intelligence dashboarding, and machine learning.
## Data Lakehouse 
### Definition
The lake house architecture approach is geared to natively integrate the best capabilities of data lakes and data warehousing, including the following:
- Ability to quickly ingest any type of data
- Storing and processing petabytes of unstructured, semi-structured, and structured data
- Support for ACID transactions (the ability to concurrently read, insert, update, and delete records in a dataset managed by the data lakehouse)
- Low latency data access
- Ability to consume data with a variety of tools, including SQL, Spark, machine learning frameworks, and business intelligence tools

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
