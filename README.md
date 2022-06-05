# Udatcity - Data Engineering Nanodegree Program
This training allow me to learn to design data models, build data warehouses and data lakes, automate data pipelines, and work with massive datasets.

* Create user-friendly relational and NoSQL data models
* Create scalable and efficient data warehouses
* Work efficiently with massive datasets
* Build and interact with a cloud-based data lake
* Automate and monitor data pipelines
* Develop proficiency in Spark, Airflow, and AWS tools


## Data Modeling
In this course, I've learned to create relational and NoSQL data models to fit the diverse needs of data
consumers. I've understood the differences between different data models, and how to choose the
appropriate data model for a given situation. I've also built fluency in PostgreSQL and Apache Cassandra.

### Contents
* Introduction to Data Modeling
    • Understand the purpose of data modeling
    • Identify the strengths and weaknesses of different types of databases and data storage techniques
    • Create a table in Postgres and Apache Cassandra
* Relational Data Models
    • Understand when to use a relational database
    • Understand the difference between OLAP and OLTP databases
    • Create normalized data tables
    • Implement denormalized schemas (e.g. STAR, Snowflake)
* NoSQL Data Models
    • Understand when to use NoSQL databases and how they differ from relational databases
    • Select the appropriate primary key and clustering columns for a given use case
    • Create a NoSQL database in Apache Cassandran

### Projects
* Data Modeling with Postgres
In this project, I've modeled user activity data for a music streaming app called Sparkify. I've created a relational database and ETL pipeline designed to optimize queries for understanding what songs users are listening to. In PostgreSQL I have also defined Fact and Dimension tables and inserted data into my new tables.
* Data Modeling with Apache Cassandra
In this project, I've modeled user activity data for a music streaming app called Sparkify. I've created a noSQL database and ETL pipeline designed to optimize queries for understanding what songs users are listening to. I've modeled my data in Apache Cassandra to allow for specific queries provided by the analytics team at Sparkify.


## Cloud Data Warehouses
I've learned to create cloud-based data warehouses. Sharpen my data warehousing skills, deepen my understanding of data infrastructure, and be introduced to data engineering on the cloud using Amazon Web Services (AWS).

#### Contents
* Introduction to the Data Warehouses
    • Understand Data Warehousing architecture
    • Run an ETL process to denormalize a database (3NF to Star)
    • Create an OLAP cube from facts and dimensions
    • Compare columnar vs. row oriented approaches
* Introduction to the Cloud with AWS
    • Understand cloud computing
    • Create an AWS account and understand their services
    • Set up Amazon S3, IAM, VPC, EC2, RDS PostgreSQ
* Implementing Data Warehouses on AWS
    • Identify components of the Redshift architecture
    • Run ETL process to extract data from S3 into Redshift
    • Set up AWS infrastructure using Infrastructure as Code (IaC)
    • Design an optimized table by selecting the appropriate distribution style and sorting key

### Project
* Build a Cloud Data Warehouse
In this project, I am tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

## Data Lake with Spark
I've learned more about the big data ecosystem and how to use Spark to work with massive datasets. I've learned about how to store big data in a data lake and query it with Spark.

#### Contents
* The Power of Spark
    • Understand the big data ecosystem
    • Understand when to use Spark and when not to use it
* Data Wrangling with Spark
    • Manipulate data with SparkSQL and Spark Dataframes
    • Use Spark for ETL purposes
* Debugging and Optimization
    • Troubleshoot common errors and optimize their code using the Spark WebUI
* Introduction to Data Lake
    • Understand the purpose and evolution of data lakes
    • Implement data lakes on Amazon S3, EMR, Athena, and Amazon Glue
    • Use Spark to run ELT processes and analytics on data of diverse sources, structures, and vintages
    • Understand the components and issues of data lakes

### Project
* Build a Data Lake
In this project, I've built an ETL pipeline for a data lake. The data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in the app. I have loaded data from S3, processed the data into analytics tables using Spark, and loaded them back into S3. I've deployed this Spark process on a cluster using AWS.

## Data Pipelines with Airflow
I've learned to schedule, automate, and monitor data pipelines using Apache Airflow. I've learned to run data quality checks, track data lineage, and work with data pipelines in production.

#### Contents
* Data Pipelines
    • Create data pipelines with Apache Airflow
    • Set up task dependencies
    • Create data connections using hooks
* Data Quality
    • Track data lineage
    • Set up data pipeline schedules
    • Partition data to optimize pipelines
    • Write tests to ensure data quality
    • Backfill data
* Production Data Pipelines
    • Build reusable and maintainable pipelines
    • Build your own Apache Airflow plugins
    • Implement subDAGs
    • Set up task boundaries
    • Monitor data pipelines

### Project
* Data Pipelines with Airflow
In this project, I've continued your work on the music streaming company’s data infrastructure by creating and automating a set of data pipelines. I've configured and scheduled data pipelines with Airflow and monitored and debuged production pipelines.

## Final Project - Capstone Project
Combine all the skills throughout the program to build my own data engineering portfolio project.

### Project
* Data Engineer Capstone
The purpose of the data engineering capstone project was to give me a chance to combine what I've learned throughout the program.
This project will be an important part of my portfolio that will help me achieve my data engineering-related career goals.
In this project, I've defined the scope of the project and the data I've been working with. I've gathered data from several different data sources; transform, combine, and summarize it; and create a clean database for others to analyze.