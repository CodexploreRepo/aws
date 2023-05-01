# AWS services for ingesting data
The first step in building big data analytic solutions is to ingest data from a variety of sources into AWS

## Amazon Database Migration Service (DMS)
- One of the most common ingestion use cases is to sync data from a traditional database system into an analytic pipeline, either landing the data in 
  - an Amazon S3-based data lake
  - a data warehousing system such as Amazon Redshift.
- `Amazon DMS` is a versatile tool that can be used to migrate existing database systems to a new database engine, such as migrating an existing Oracle database to an Amazon Aurora with PostgreSQL compatibility database. 
- But from an analytics perspective, Amazon DMS can also be used to run continuous replication from a number of common database engines into an Amazon S3 data lake.

### How Amazon DMS works
- do an initial load of data from the databases into S3, specifying the format that we want the file written out in (CSV or Parquet), and the specific ingestion location in S3.
- At the same time, we can also set up a DMS task to do ongoing replication from the source databases into S3 once the full load completes
- With transactional databases, the rows in a table are regularly updated, such as if a customer changes their address or telephone number. 
- DMS uses the **database transaction log files** from the database to track updates to rows in the database and writes out the target file in S3 with an extra column added (`Op`) that indicates which operation is reflected in the row – an insert, update, or deletion.
  - For example: a source table with a schema of `custid`, `lastname`, `firstname`, `address`, and `phone`, and the following sequence of events happens:
    - A new customer is added with all fields completed.
    - The phone number was entered incorrectly, so the record has the phone number updated.
    - The customer record is then deleted from the database.
