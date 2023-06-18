# S3 Commands

- To create an S3 bucket: `aws s3 mb s3://<bucket-name>`
  - Note: bucket name must be globally unique
- To download: `aws s3 sync s3://YOUR_BUCKET . --quiet --exclude "*.png"
`
