# AWS Glue PySpark

## Appendix
### Logger
- In order to print in Glue console, need to get `logger` of Glue Context
```Python
# set custom logging on
logger = glueContext.get_logger()
```