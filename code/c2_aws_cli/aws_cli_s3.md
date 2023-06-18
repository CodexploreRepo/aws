# S3 Commands

- To create an S3 bucket: `aws s3 mb s3://<bucket-name>`
  - Note: bucket name must be globally unique
- To upload a file: `aws s3 cp test.csv s3://your-bucket-name/`
- To upload multiple files: `aws s3 cp . s3://your-bucket-name/ --recursive --exclude "*.jpg"  --include "*.log"`
  - `.` represents the current directory.
  - `--recursive` is used to upload all files and subdirectories recursively.
- To download: `aws s3 sync s3://YOUR_BUCKET . --quiet --exclude "*.png"
`
