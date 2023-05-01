# AWS Services for Transforming Data
- Once your data is ingested into an appropriate AWS service, such as Amazon S3, the next stage of the pipeline needs to transform the data to optimize it for analytics and to make it available to your data consumers.

## AWS Lambda for Light Transformations
- AWS Lambda provides a serverless environment for executing code and is one of AWS's most popular services.
- Lambda is also massively parallel, meaning that it can easily scale for highly concurrent workloads. 
  - By default, you can have 1,000 concurrent Lambda executions within an AWS Region for your account, but you can work with AWS support to increase this limit into the hundreds of thousands. 
- For example, you may receive a ZIP file containing hundreds of XML files, and in your Lambda function you want to unzip the file, and then for each file you want to validate that it is valid XML, perform calculations on fields in the file to update various other systems, concatenate the contents of all the files, and write that out in Parquet format in a different zone of your data lake.

## AWS Glue for Serverless Spark Processing
- AWS Glue has multiple components that could have been split into multiple separate services, but these components can all work together, and so AWS has grouped them together into the AWS Glue family.

### Serverless ETL processing
- At the heart of AWS Glue is a serverless environment providing either 
  - **Python engine** (known as `Glue Python shell`)
    - Python, which runs on a single node, has become an extremely popular language for performing data engineering-related tasks in scenarios where the power of a multi-node cluster is not required. 
  - **Apache Spark engine** for performing data transformations and processing. Python can be used for performing transformations on small to medium datasets, while Apache Spark enables optimal processing for very large datasets:
    - Apache Spark is an open source engine for distributed processing of large datasets across a cluster of compute nodes, which makes it ideal for taking a large dataset, splitting the processing work among the nodes in the cluster, and then returning a result. As Spark does all processing in memory, it is highly efficient and performant and has become the tool of choice for many organizations looking for a solution for processing large datasets.
- Both engines can work with data that resides in Amazon S3, and with the `AWS Glue Data Catalog`. 
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/235410534-647b2277-e384-426e-b307-c813e7024205.png"><br>Glue Python shell and Glue Spark engines</p>

### AWS Glue Data Catalog
- To complement the ETL processing functionality, AWS Glue also includes a `data catalog` that can be used to provide a logical view of data stored physically on a disk, and objects in the catalog can then be directly referenced from your ETL code.
- The AWS Glue Data Catalog is a **Hive metastore-compatible catalog**, i.e. the AWS Glue catalog works with a variety of other services and third-party products that can integrate with Hive metastore-compatible catalogs.
- For example, the data catalog consists of a number of databases at the top level (such as the HR database), and each database contains one or more tables (such as the Employee table), and each table contains metadata, such as the column headings and data types for each column (such as employee_id, lastname, firstname, address, and dept), as well as references to the S3 location for the data that makes up that table.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/235410930-642298ab-1439-4980-9be8-4a89fe71eb9c.png"><br>AWS Glue Data Catalog showing a logical view of the Employee table</p>

### AWS Glue crawlers
- AWS Glue crawlers are processes that can examine a data source (such as a path in an S3 bucket) and automatically infer the schema and other information about that data source, so that the AWS Glue Data Catalog can be automatically populated with relevant information.
- For example, we could point an AWS Glue Crawler at the S3 location where DMS replicated the Employee table of our HR database. When the Glue Crawler runs, it examines a portion of each of the files in that location, identifies the file type (CSV, Parquet), uses a classifier to infer the schema of the file (column headings and types), and then adds that information into a database in the Glue catalog.

## Amazon EMR for Hadoop Ecosystem Processing
- Amazon EMR provides a managed platform for running popular open source big data processing tools, such as Apache Spark, Apache Hive, Apache Hudi, Apache HBase, Presto, Pig, and others. 
- Amazon EMR takes care of the complexities of deploying these tools and managing the underlying clustered Amazon EC2 compute resources.
- You might be wondering why AWS has two services (Amazon EMR & AWS Glue) that effectively offer the same big data processing engine. 
  - AWS Glue offers a serverless environment for running Apache Spark
     -  AWS Glue you pay a slightly higher cost for an equivalent sized server than you would with Amazon EMR, but AWS Glue requires far less understanding or experience with regard to running an Apache Spark environment 
  - Amazon EMR you need to specify the detailed configuration of the cluster you want to run Apache Spark.
     - If your use case would benefit from being able to more finely tune the environment where Apache Spark runs, then Amazon EMR would be a better fit as it provides more options for specifying the configuration of the compute cluster and Spark settings than AWS Glue allows  
- The other important differentiator is that Amazon EMR offers many additional frameworks and tools for big data processing such as Apache Hive, Presto, or other toolsets supported in EMR, then Amazon EMR would be a great fit.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/235547401-027ae44b-1eba-45e7-b26f-af5ab62cdabb.png"><br>High-level overview of an EMR cluster</p>

- Each EMR cluster requires 
  - a master node
  - at least one core node (a worker node that includes local storage)
  - optionally a number of task nodes (worker nodes that do not have any local storage).


