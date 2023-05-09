# Terminology

- **Amazon Resource Names** (ARNs) uniquely identify AWS resources.
- **Change Data Capture (CDC)** the process of tracking and recording the changes such as using the database transaction log files from the database to track updates to rows in the database and writes out the target file in S3 with an extra column added (Op) that indicates which operation is reflected in the row – an insert, update, or deletion.
- **Data Mart** is focused on a single business subject repository (for example, marketing, sales, or finance) and is typically created to serve a narrower group of business users, such as a single department.
- **Database Migration Service (DMS)** sync data from a traditional database system into an analytic pipeline, either landing the data in an Amazon S3-based data lake, or in a data warehousing system such as Amazon Redshift
- **EDW** (Enterprise Data Warehouse) is the central data repository that contains structured, curated, consistent, and trusted data assets that are organized into a well-modeled schema
- **Governed table**: With governed tables, users can run transactional queries against data stored in the table, including inserts, updates, and deletes. In addition to this, with governed tables, users can time travel, which means they can query a table and specify a specific time, and the results that are returned will represent the data as it was at the specified point in time.
- **Massively Parallel Processing** (MPP) cloud data warehouses implement a distributed query processing architecture called (MPP) to accelerate queries on massive volumes of data.
- **MSK** Managed Streaming for Apache Kafka
- **MWAA** Managed Workflows for Apache Airflow
- **S3** Amazon Simple Storage Service
- **Serverless** meaning that you do not need to deploy or manage any infrastructure, and you pay for the service based on your usage, not on fixed infrastructure costs.
- **Virtual Private Cloud (Amazon VPC)**, the private network in your AWS account, gives you full control over your virtual networking environment, including resource placement, connectivity, and security.

# Python Packages

- `AWS Data Wrangler`, created by AWS Professional Services to simplify common ETL tasks when working in an AWS environment, such as to convert a CSV file into Parquet format or infer schema & update the AWS Glue Data Catalog
