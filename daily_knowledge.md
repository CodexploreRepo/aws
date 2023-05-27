# Daily Knowledge
## Day 1
###  Managing Identity and Permissions
Two primary ways to manage which identities can access which resources:
1. `AWS Identity and Access Management (IAM`) service
  - **Federation of identities** meaning that you can configure IAM to use another identity provider for authentication, such as Active Directory or Okta.
2. `AWS Lake Formation` to manage data lake access
### Data Encryption
- **AWS Key Management Service (KMS)** is to create and manage security keys for encrypting and decrypting data in AWS.
  -  For example, in Amazon S3, you can enable **Amazon S3 Bucket Keys**, which configures an S3 Bucket Key to encrypt all new objects in the bucket with an AWS KMS Key. 
- **AWS CloudTrail** is to log all use of AWS KMS keys. 
### Data Catalog
- 2 types of data catalogs: business catalogs and technical catalogs
- Within AWS, there are two services for interacting with the data catalog: `AWS Glue service`, `AWS Lake Formation`
### Data Lakehouse
- **Data LakeHouse** store the data in S3 (data lake) and use Redshift Serverless as a processing platform along with Redshift Spectrum instead of maintaining Redshift Cluster as a Data Warehouse since maintaining Redshift Cluster is quite expensive
### Concepts
- **Authentication** is the process of validating that a claimed identity is that identity.
- **Authorization** is the process of authorizing access to a resource based on a validated identity.
- **Data security** dictates how an organization should protect data to ensure that data is stored securely (such as in an encrypted state) and that access by unauthorized entities is prevented.
- **Data governance** is related to ensuring that only people that need access to specific datasets to perform their job is granted the access.
  - Governance also applies to ensuring that an organization only uses and processes data on individuals in approved ways and that organizations provide data disclosures as required by law.

