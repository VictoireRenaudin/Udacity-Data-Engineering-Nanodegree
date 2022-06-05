# Project: Data Modeling with Postgres

## Project instructions
### Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

### Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Project answers 
## Purpose of this database 
Sparkify needs a database to understand which songs are listening to and which is the popularity of different songs and artists. This database aggregate all songs, artits, songplays and also users who listen the songs. 

## Functionning of Python scripts
To use these scripts, first you will have to run create_tables.py and then etl.py.

## Explanations of files in the repository 

**- test.ipynb** : This Jupyter notebook is used to validate our Python scripts. Thanks to it, we can have a look on our tables and be sure the work is done correctly.

**- sql_queries.py** : This Python script contains SQL queries for deleting and creating tables, and inserting data into them.  

**- create_tables.py** : This Python script contains code for setting up our database (deleting and creating tables). 

**- etl.ipynb** : This Jupyter notebook is used to analyse our data and to prepare queries for loading data into tables. 

**- etl.py** : This Python script is used to insert all data in our tables.

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
    
**- artists** : This table contains all artists. 
    - artist_id
    - name
    - location
    - latitude
    - longitude

**- songs** : This table contains all songs.
    - song_id
    - title
    - artist_id
    - year
    - duration

**- time** :
    - start_time
    - hour
    - day
    - week
    - month
    - year
    - weekday

**- users** : This table contains all users.
    - user_id
    - first_name
    - last_name
    - gender
    - level