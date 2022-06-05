# Project: Data Warehouse

## Project instructions
### Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

### Project Description
In this project, you'll apply what you've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, you will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

## Project answers 

## Explanations of files in the repository 

**- create_tables.py** : This Python script contains code for setting up our database (deleting and creating fact and dimension tables for the star schema in Redshift). 

**- etl.py** : This Python script is used to load data from S3 into staging tables on Redshift and then process that data into analytics tables on Redshift.

**- sql_queries.py** : This Python script is used to define the SQL statements which will be imported into the two other files above. 

## Database schema design and ETL pipeline
We use a star schema with fact and dimension tables: 

### Fact table :

**- songplays** : This table contains all songplays. 
    - songplay_id
    - start_time
    - user_id
    - level
    - song_id 
    - artist_id
    - session_id
    - location, 
    - user_agent

### Dimensions tables :
    
**- artists** : This table contains all artists in music database. 
    - artist_id
    - name
    - location
    - latitude
    - longitude

**- songs** : This table contains all songs in music database.
    - song_id
    - title
    - artist_id
    - year
    - duration

**- time** : This table contains timestamps of records in songplays broken down into specific units. 
    - start_time
    - hour
    - day
    - week
    - month
    - year
    - weekday

**- users** : This table contains all users in the app.
    - user_id
    - first_name
    - last_name
    - gender
    - level