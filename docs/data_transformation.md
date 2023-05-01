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
  - a Python engine (known as `Glue Python shell`)
    - Python, which runs on a single node, has become an extremely popular language for performing data engineering-related tasks in scenarios where the power of a multi-node cluster is not required. 
  - Apache Spark engine for performing data transformations and processing. Python can be used for performing transformations on small to medium datasets, while Apache Spark enables optimal processing for very large datasets:
    - Apache Spark is an open source engine for distributed processing of large datasets across a cluster of compute nodes, which makes it ideal for taking a large dataset, splitting the processing work among the nodes in the cluster, and then returning a result. As Spark does all processing in memory, it is highly efficient and performant and has become the tool of choice for many organizations looking for a solution for processing large datasets.
