from urllib.parse import unquote_plus

import awswrangler as wr


def lambda_handler(event, context):
    # Get the source bucket and object name as passed to the Lambda function
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        # unquote: replace %xx escapes with their single-character equivalent.
        #  -> unquote('/El%20Ni%C3%B1o/') yields '/El Niño/'
        # unquote_plus: replace plus signs with spaces, as required for unquoting HTML form values.
        # -> unquote_plus('/El+Ni%C3%B1o/') yields '/El Niño/'
        key = unquote_plus(record["s3"]["object"]["key"])

    # We will set the DB and table name based on the last two elements of
    # the path prior to the file name. If key = 'dms/sakila/film/LOAD01.csv',
    # then the following lines will set db to sakila and table_name to 'film'
    key_list = key.split("/")
    # key_list: ['testdb', 'csvparquet', 'test.csv']
    print(f"key_list: {key_list}")
    db_name = key_list[len(key_list) - 3]
    table_name = key_list[len(key_list) - 2]

    print(f"Bucket: {bucket}")  # Bucket: upskills-landing-zone
    print(f"Key: {key}")  # Key: testdb/csvparquet/test.csv
    print(f"DB Name: {db_name}")  # DB Name: testdb
    print(f"Table Name: {table_name}")  # Table Name: csvparquet

    input_path = f"s3://{bucket}/{key}"
    # Input_Path: s3://upskills-landing-zone/testdb/csvparquet/test.csv
    print(f"Input_Path: {input_path}")

    output_path = f"s3://upskills-clean-zone/{db_name}/{table_name}"
    # Output_Path: s3://upskills-clean-zone/testdb/csvparquet
    print(f"Output_Path: {output_path}")

    input_df = wr.s3.read_csv([input_path])

    current_databases = wr.catalog.databases()
    wr.catalog.databases()
    if db_name not in current_databases.values:
        print(f"- Database {db_name} does not exist ... creating")
        wr.catalog.create_database(db_name)
    else:
        print(f"- Database {db_name} already exists")
    try:
        result = wr.s3.to_parquet(
            df=input_df,
            path=output_path,  # s3://upskills-clean-zone/testdb/csvparquet
            dataset=True,  # There is no need .parquet in the output path
            database=db_name,  # Glue/Athena catalog
            table=table_name,  # Glue/Athena catalog
            mode="append",
        )
    except Exception as e:
        print(f"Error {e}")
    print("RESULT: ")
    print(f"{result}")

    return result
