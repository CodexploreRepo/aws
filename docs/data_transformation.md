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
- For example, the data catalog consists of a number of databases at the top level (such as the HR database), and each database contains one or more tables (such as the Employee table), and each table contains metadata, such as the column headings and data types for each column (such as employee_id, lastname, firstname, address, and dept), as well as references to the S3 location for the data that makes up that table.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/235410930-642298ab-1439-4980-9be8-4a89fe71eb9c.png"><br>AWS Glue Data Catalog showing a logical view of the Employee table</p>

