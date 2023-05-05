# Big Data Pipeline Orchestration
- Data pipeline can be built to bring in data from source systems &#8594; transform that data through multiple stages &#8594; further transforming or enriching the data as it moves through each stage.
- Each pipeline may use multiple services to achieve the goals of the pipeline and orchestrating all the varying services and pipelines can be complex. 

## AWS Glue Workflows for orchestrating Glue components
- AWS Glue includes a number of components as follows:
  - `Serverless Apache Spark` or `Python shell` environment for performing ETL transformations
  - `Glue Data Catalog`, which provides a centralized logical representation (database and tables) of the data in an Amazon S3 data lake
  - `Glue crawlers` which can be configured to examine files in a specific location, automatically infer the schema of the file, and a
- **AWS Glue workflows** are a functionality within the AWS Glue service and have been designed to help orchestrate the various AWS Glue components
  -  A workflow consists of an ordered sequence of steps that can run Glue crawlers and Glue ETL jobs (Spark or Python shell).
  - This workflow orchestrates the following tasks:
    - It runs a Glue Crawler to add newly ingested data from the raw zone of the data lake into the Glue data catalog.
    - Once the Glue Crawler completes, it triggers a Glue ETL job to convert the raw CSV data into Parquet format, and writes to the curated zone of the data lake.
    - When the Glue job is complete, it triggers a Glue Crawler to add the newly transformed data in the curated zone, into the Glue data catalog.
<p align="center"><img width=600 src="https://user-images.githubusercontent.com/64508435/236497490-fac2dc43-06d6-4dca-a266-0155caf30d80.png"><br>AWS Glue workflow</p>

 ## AWS Step Functions for complex workflows
 - Another option for orchestrating your data transformation pipelines is **AWS Step Functions**, a service that enables you to create complex workflows that can be integrated with many AWS services.
 - With Step Functions, you use `JSON` to define a state machine using a structured language known as the Amazon States Language. 
 - **Step Functions Workflow Studio** to create a workflow using a visual interface that supports drag and drop.
 - You can trigger a step function using `Amazon EventBridge` (such as on a schedule or in response to something else triggering an EventBridge event event) or can trigger the step function on-demand by calling the Step Functions API.
<p align="center"><img width=400 src="https://user-images.githubusercontent.com/64508435/236501773-98c1fd90-80e4-4949-b945-89a2e1430753.png"><br>AWS Step Functions state machine</p>

1. A **CloudWatch** event is triggered whenever a file is uploaded to a particular Amazon S3 bucket, and the CloudWatch event starts our state machine, passing in a JSON object that includes the location of the newly uploaded file.
2. The first step, **Process Incoming File**, runs a Glue Python shell job that takes the location of the uploaded file as input and processes the incoming file (for example, converting from CSV to Parquet format).
3. The Did Job Succeed? step is of type Choice. It examines the JSON data passed to the step, and if the jobStatus field is set to succeeded, it branches to Run AWS Glue Crawler. If the jobStatus field is set to failed, it branches to Job Failed.
4. In the Run AWS Glue Crawler step, a Lambda function is triggered, which in turn triggers an AWS Glue Crawler to run against the location where the previous Lambda function had written the Parquet file. 

## Amazon managed workflows for Apache Airflow
- **Apache Airflow** is a popular open source solution for orchestrating complex data engineering workflows. 
- Since installing and configuring Apache Airflow is complex, AWS created **Managed Workflows for Apache Airflow (MWAA)**, which enables users to easily deploy a managed version of Apache Airflow that can automatically scale out additional workers as demand on the environment increases, and scale in the number of workers as demand decreases.
- An MWAA environment consists of the following components:
  - **Scheduler**: The scheduler runs a multi-threaded Python process that controls what tasks need to be run, and where and when to run those tasks.
  - **Worker/executor**: The worker/s execute/s tasks. Each MWAA environment contains 
    - at least one worker (can specify the maximum number of additional workers that should be made available, MWAA automatically scales out the number of workers up to that maximum but will also automatically reduce the number of workers as tasks are completed and if no new tasks need to run) 
    - The workers are linked to your VPC (the private network in your AWS account).
  - **Meta-database**: This runs in the MWAA service account and is used to track the status of tasks.
  - **Web server**: The web server also runs in the MWAA service account and provides a web-based interface that users can use to monitor and execute tasks.
