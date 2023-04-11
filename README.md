# <p align="center">Kayak: plan your trip</p>

![Kayak](https://seekvectorlogo.com/wp-content/uploads/2018/01/kayak-vector-logo.png)

## Video presentation

[Kayak - Video presentation](https://share.vidyard.com/watch/wu4KAETvzEQBys6gG3rtUk?)

## Contact

You can write me at **alexon.uthayakumar@gmail.com**

## Context 

<a href="https://www.kayak.com" target="_blank">Kayak</a> is a travel search engine that helps user plan their next trip at the best price.

The marketing team needs help on a new project. After doing some user research, the team discovered that **70% of their users who are planning a trip would like to have more information about the destination they are going to**. 

In addition, user research shows that **people tend to be defiant about the information they are reading if they don't know the brand** which produced the content. 

Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:

* Weather 
* Hotels in the area 

The application should then be able to recommend the best destinations and hotels based on the above variables at any given time. 

Marketing team wants to focus first on the top-35 cities to travel to in France, as chosen by <a href="https://one-week-in.com/35-cities-to-visit-in-france/" target="_blank">One Week In.com</a>

## Goal of the project
Obtain information on destinations from the top-35 cities list:
- GPS coordinates of the destination,
- Weather data for each destination,
- Hotel data for each destination.

The information should be combined in a single table containing enriched information about weather and hotels for each destination and stored in an S3 bucket. The same cleaned data should also be avalable as an SQL Database.

Based on this data, two maps should be delivered :
- Top-5 destinations,
- Top-20 hotels in these destinations.


## Project files

1. **kayak_scraper** folder is where the package **scrapy** to scrape the **Booking.com** hotels.
2. [**weather.ipynb**](weather.ipynb) is a notebook where we use external api's to collect wheather data.
3. [**data**](data/) is a folder where all the data was stored before storing it in a Data Lake like S3 bucket.
4. [**final.ipynb**](final.ipynb) is a notebook where all the data was gathered, ETL processes  and some visualizations to achive the goal. 

## Keys and credentials

API key for openweathermap.org as well as AWS credentials should be provided in the [**final.ipynb**](final.ipynb) and [**weather.ipynb**](weather.ipynb) notebooks.