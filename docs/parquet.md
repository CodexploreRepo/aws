# Parquet
## How a Hive table is stored as a parquet file
- Compression Type: **snappy**
- For example, the Hive `secmaster` table is partitioned by `country` and `datetrading` columns
  - If you read the file *7f1fc52c7a574e7ca12f26bd61ed1223.snappy.parquet* directly, there will be 2 missing columns which are `country` and `datetrading` columns
<p align='center'><img src="https://github.com/CodexploreRepo/aws/assets/64508435/9b7ec57e-270a-42fb-ba07-5ecb50d48fad" width='600'/></p>
