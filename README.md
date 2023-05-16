# Spotify ETL Data Engineering Project

## Intro

In this project, a ETL pipeline using Spotify API and AWS was build. The pipelin retrieves data from the Spotify API, transform it to a desired format, and load it into an AWS data store. 

### Architecture
![Architecture Diagram](https://github.com/JKUOL/Spotify_data_pipeline/blob/main/ETL_schema.png)

### Dataset/API

[Spotify API](https://developer.spotify.com/documentation/web-api) containing information among other things, about artists, albumbs and songs 

### Services Used

1. **Amazon S3 (Simple Storage Services)**

2. **AWS Lamda**

3. **Cloud Watch**

4. **Glue Crawler**

5. **Data Catalog**

6. **Amazon Athena**


### Install Packages
```
pip install pandas
pip install spotipy
```
Project Execution Flow

Extrac Data from API -> Lamda Trigger (choosen frequency) -> Run extract Code -> Store the Raw Data -> Trigger the Transform Function -> Transform the Data and load it -> Query using Athena
