# AWS Lake Formation
## Setup
- Step 1: An IAM user with the `AWSLakeFormationDataAdmin` policy
- Step 2: Create a data lake administrator - designate yourself a data lake administrator to allow access to any Lake Formation resource.
<p align="center"><img width="603" alt="Screenshot 2023-06-17 at 18 30 26" src="https://github.com/CodexploreRepo/aws/assets/64508435/ec922d02-e91b-453a-89ec-6ec9d5de7f31"></p>

  - Once registered, you can find IAM user as Data Lake Administrator at `Permission` &#8594; `Administrative roles and tasks`
  <p align="center"><img width="600" src="https://github.com/CodexploreRepo/aws/assets/64508435/75b5c419-de73-47bf-9c22-2bb5eea8b0d8"></p>

- Step 3: Register the S3 as **Data Lake locations** 
<p align="center"><img width="800" alt="Screenshot 2023-06-17 at 19 00 46" src="https://github.com/CodexploreRepo/aws/assets/64508435/ea877c06-bfc3-4841-a49f-033a803c0f12"></p>


- Step 4: Create a new database
  - Uncheck "Use only IAM access control for new tables in this database" since we will use Lake Formation to control the access of tables in the database
<p align="center"><img width="600" alt="Screenshot 2023-06-17 at 18 53 47" src="https://github.com/CodexploreRepo/aws/assets/64508435/b1df2f53-6a51-47c0-bf25-66796f6bb9c1"></p>

- Step 5: Create Table in a database
  - Note: you have to Grant Permission to the table 
<p align="center"><img width="690" alt="Screenshot 2023-06-17 at 19 15 45" src="https://github.com/CodexploreRepo/aws/assets/64508435/09a46907-7f7b-4248-9296-0195c32700cf"></p>


