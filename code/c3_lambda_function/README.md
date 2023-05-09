# AWS Lambda function

## Lab 1: AWS Lambda Function Triggering

### Lab Objective

- **Lab**: triggering an AWS Lambda function when a new file arrives in an S3 bucket
  - **Task**: configure an S3 bucket to automatically trigger a Lambda function whenever a new file is written to the bucket.
    - In the Lambda function, an open source Python library called `AWS Data Wrangler`, created by AWS Professional Services to simplify common ETL tasks when working in an AWS environment, is used to convert a CSV file into Parquet format, and then update the AWS Glue Data Catalog.

### Creating a `Lambda layer` containing `AWS Data Wrangler` library

- `Lambda layers` allow your Lambda function to bring in additional code, packaged as a .zip file.
- By creating a Lambda layer for the AWS Data Wrangler library, we can use AWS Data Wrangler in any of our Lambda functions just by ensuring this Lambda layer is attached to the function.
  - AWS Data Wrangler library in GitHub at [https://github.com/awslabs/aws-data-wrangler/releases](https://github.com/awslabs/aws-data-wrangler/releases). Under **Assets**, download the awswrangler-layer-3.0.0-py3.9.zip file to your local drive.
  - In the top search bar of the **AWS console**, search for and select the **Lambda** service.
  - In the left-hand menu, under **Additional Resources**, select **Layers**, and then click on Create layer.
  - For **Compatible runtimes** choose `optional`, select Python 3.9 and then click Create.
    <img src="../.././assets/img/c3_aws_lambda_layer.png">

### Creating new Amazon S3 buckets

- It is common for data lake to have multiple zones for the data to move through.
- _Note_: ensure the bucket is in the same region with the Lambda function
  - **Landing Zone** (for ingestion of raw files) (e.g. `upskills-landing-zone`)
  - **Clean zone** (for files that have undergone initial processing and optimization) (e.g. `upskills-clean-zone`)

### Creating an IAM policy and role for Lambda function

#### Creating an IAM policy

- For this project, ensure that our Lambda function has the following permissions:
  - Read our source S3 bucket
  - Write to our target S3 bucket (for example, dataeng-clean-zone-<initials>)
  - Write logs to Amazon CloudWatch
  - Access to all Glue API actions (to enable the creation of new databases and tables)
- To create a new AWS IAM role with these permissions, follow these steps:
  - Step 1: From the Services dropdown, select the **IAM service**, and in the left-hand menu, select **Policies** and then click on **Create policy**.
    - By default, the Visual editor tab is selected, so change to the **JSON** tab.
- Step 2: copy the [S3, Cloud Watch, & Glue Policy](./lab01/DataEngLambdaS3CWGluePolicy.json) to the **JSON** tab

  - This first block of the policy configures the policy document and provides permissions for using **CloudWatch** log groups, log streams, and log events

  ```json
  {
    "Effect": "Allow",
    "Action": [
      "logs:PutLogEvents",
      "logs:CreateLogGroup",
      "logs:CreateLogStream"
    ],
    "Resource": "arn:aws:logs:*:*:*"
  }
  ```

  - This next block of the policy provides permissions for all **Amazon S3** actions (get and put) that are in the Amazon S3 bucket specified in the resource section (in this case, our clean-zone and landing-zone buckets)

  ```json
  {
    "Effect": "Allow",
    "Action": ["s3:*"],
    "Resource": [
      "arn:aws:s3:::upskills-landing-zone/*",
      "arn:aws:s3:::upskills-landing-zone",
      "arn:aws:s3:::upskills-clean-zone/*",
      "arn:aws:s3:::upskills-clean-zone"
    ]
  }
  ```

  - In the final statement of the policy, we provide permissions to use all **AWS Glue** actions (create job, start job, and delete job).
    - **Note**: that in a production environment, you should limit the scope specified in the resource section:

  ```json
  {
    "Effect": "Allow",
    "Action": ["glue:*"],
    "Resource": "*"
  }
  ```

- Step 3: Provide a name for the policy, such as `DataEngLambdaS3CWGluePolicy`, and then click **Create policy**.

#### Creating an IAM role

- In the left-hand menu, click on **Roles** and then **Create role**.
- For trusted entity, ensure **AWS service** is selected, and for service, select **Lambda** and then click Next: Permissions.
  - In the next section (Creating a Lambda function), we will assign this role to our Lambda function.
- Under **Attach permissions**, select the policy we just created (for example, `DataEngLambdaS3CWGluePolicy`) by searching and then clicking in the tick box. Then click **Next: Tags**.
- Provide any tags you would like associated with this policy (optional) and click **Next: Review**.
- Provide a role name, such as `DataEngLambdaS3CWGlueRole`, and click **Create role**.

### Creating a Lambda function

- Goal: to create our Lambda function that will be triggered whenever a CSV file is uploaded to our source S3 bucket. The uploaded CSV file will be converted to Parquet, written out to the target bucket, and added to the Glue catalog using AWS Data Wrangler:
  -Step: In the **AWS console**, from the **Services** dropdown, select the **Lambda** service, and in the left-hand menu select **Functions** and then click **Create function**.
- Step 2: Select **Author from scratch** and provide a function name (such as CSVtoParquetLambda).
  - For Runtime, select Python from the drop-down list.
  - Expand Change default execution role and select **Use an existing role** & select the role you created in the previous section (such as `DataEngLambdaS3CWGlueRole`)
  - Do not change any of the advanced settings and click **Create function**.
- Step 3: Click on Layers in the first box, and then click Add a layer in the second box.
- Step 4: Define the lambda function [CSVtoParquetLambda](./lab01/CSVtoParquetLambda.py)
- Step 5: Increase the timeout to 1 min & memory limit (256MB):
  - Click on the **Configuration** tab, and on the left-hand side click on **General configuration**. Click the Edit button and modify the Timeout to be 1 minute (the default timeout of 3 seconds is likely to be too low to convert some files from CSV to Parquet format).

#### Configuring the Lambda function to be triggered by an S3 upload

- In the Function Overview box of our Lambda function, click on Add trigger.
- For Trigger configuration, select the Amazon S3 service from the drop-down list.
- For Bucket, select your landing zone bucket.
- We want our rule to trigger whenever a new file is created in this bucket, no matter what method is used to create it (Put, Post, or Copy), so select** All object create events** from the list.
- For suffix, enter `.csv`. This will configure the trigger to only run the Lambda function when a file with a .csv extension is uploaded to our landing-zone bucket.

#### Testing the Lambda function

- Upload your test file to your source S3 bucket:

```bash
aws s3 cp test.csv s3://upskills-landing-zone/testdb/csvparquet/test.csv
```

- If everything has been configured correctly, your Lambda function will have been triggered and
  - Will have written out a Parquet-formatted file to your target S3 bucket
  - created a Glue datalog for the table.

```bash
aws s3 ls s3://upskills-clean-zone/testdb/csvparquet/
```

## Common Error

Error 1: Memory Size: 128 MB Max Memory Used: 128 MB

- Reason: it was running out of memory on my Lambda function execution, updating the max memory, and the issue was resolved.

```bash
REPORT RequestId: 4f8dc5b8-ae49-48ff-b3f1-d220ed884caf	Duration: 62056.99 ms	Billed Duration: 60000 ms	Memory Size: 128 MB	Max Memory Used: 128 MB	Init Duration: 4068.61 ms
```
