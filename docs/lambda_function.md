# AWS Lambda
## Lambda Layer
- `Lambda layers` allow your Lambda function to bring in additional code, packaged as a .zip file.
  - For example, an zip file of AWS Data Wrangler library in GitHub at [https://github.com/awslabs/aws-data-wrangler/releases](https://github.com/awslabs/aws-data-wrangler/releases). 
    - Under **Assets**, download the `awswrangler-layer-3.0.0-py3.9.zip` file to your local drive

### How to install a pacakge in Lambda 
- AWS Lambda works on Linux, only package that are **compiled** to run under a **Linux** environment can be used here.
  - For ex: `pandas` wheel (complied) file which works for Python 3.7 on AWS Lambda is `pandas-1.0.3-cp37-cp37m-manylinux1_x86_64.whl`
- How to prepare the packages as a Lambda layer:
  - Step 1: To get the linux compiled file, say `pandas`, `xldr`, `numpy` packages, go to the link: https://pypi.org/project/pandas/#files and download the relevant wheel (.whl) file.
  - Step 2: Create a folder named `python` (This name is very important)
  - Step 3: Once the folder is created, unzip the `.whl` files in the `python` folder as follows:
    - <img width="283" alt="Screenshot 2023-06-17 at 14 12 25" src="https://github.com/CodexploreRepo/aws/assets/64508435/82aeedc4-8c0e-4be9-8bfc-cfb344cede9b">
  - Step 4: zip the `python` folder to `python.zip` and add to Lambda layer
    - NOTE: you can rename `python.zip` into other name after it is being zipped
