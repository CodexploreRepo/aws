# AWS Glue

## AWS Glue Table

- The Glue table is the metadata definition that represents your data in schema form.
  - This can be created via `Glue Crawler`

## AWS Glue Connection

## AWS Glue Job

- To perform ETL work which including a transformation script, data sources, and data targets
- Job runs are initiated by **triggers** that can be scheduled or triggered by events

## AWS Glue Trigger

### Trigger from Lambda function

- You can trigger a glue job from the lambda function

```Python
import boto3

def lambda_handler(event, context):
  # Trigger the glue ETL job
  client = boto3.client("glue")
  glue_response = client.start_job_run(JobName=os_glue_job_name)
  print(f"Starting glue job {os_glue_job_name}:\{glue_response}")
  return glue_response
```
