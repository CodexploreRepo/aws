# AWS Command Line Interface tool

## AWS CLI Installation & Configuration

- Step 1: Download the appropriate AWS CLI installer for your platform (Mac, Windows, or Linux) from https://aws.amazon.com/cli/.
- Step 2: Run the installer to complete the installation of the AWS CLI.
- Step 3: To configure the CLI, run `aws configure` at the Command Prompt and
  - provide the AWS Access Key ID and AWS Secret Access Key for your IAM Administrative user.
  - Also, provide a default region. In my case is `ap-southeast-1` (Singapore)
- **Note**: If you already have the AWS CLI configured and associated with a different IAM user account, you have the option of configuring multiple profiles, each one associated with a different IAM user.

```bash
$ aws configure --profile quannguyen
AWS Access Key ID [None]: <get-from-IAM-user-console>
AWS Secret Access Key [None]: <get-from-IAM-user-console>
Default region name [None]: ap-southeast-1
Default output format [None]: ENTER

# Testing: access the s3 bucket with the profile "quannguyen" just created
$ aws s3 ls --profile quannguyen
2023-05-07 22:13:26 upskills-clean-zone
2023-05-07 23:08:35 upskills-landing-zone
```

- To list profiles configured: `aws configure list-profiles`
- Set default profiles:

```bash
export AWS_DEFAULT_PROFILE=MyProfile
# To make the change persistent, add the above line into your ~/.bashrc user's file or or ~/.zshrc


# then switch back to the default profile using
# 'default' is the profile name given to your first profile when you create it.
export AWS_DEFAULT_PROFILE=default
```

## AWS Config

- AWS Config file is located at `~/.aws/config` in your PC
- You can set `export AWS_DEFAULT_PROFILE=quannguyen`

## S3 Commands

- To create an S3 bucket: `aws s3 mb s3://<bucket-name>`
  - Note: bucket name must be globally unique
- To upload a file: `aws s3 cp test.csv s3://your-bucket-name/`
- To upload multiple files: `aws s3 cp . s3://your-bucket-name/ --recursive --exclude "*.jpg"  --include "*.log"`
  - `.` represents the current directory.
  - `--recursive` is used to upload all files and subdirectories recursively.
- To download: `aws s3 sync s3://YOUR_BUCKET . --quiet --exclude "*.png"
`
