Create scrapy project with:

```
$ pip install scrapy

# see all available commands
$ scrapy

$ scrapy startproject kayak_scraper

$ cd kayak_scraper

# you can start your first spider with:
$ scrapy genspider <<name>> <<url>>
$ scrapy genspider hotels_spider https://www.booking.com/searchresults.html

# Run a spider inside the project
$ scrapy crawl hotels_spider

# Storing the scraped data
  -O : overwrites any existing file, 
  -o : append new content to any existing file )
$ scrapy crawl hotels_spider -O src/hotels.json

# Run a self-contained spider (without creating a project)
$ scrapy runspider hotels_spider.py

# You can test scraping in a shell
$ scrapy shell https://www.booking.com/searchresults.html?ss=Paris
$ response.xpath('//*[@id="search_results_table"]/div[2]/div/div/div/div[4]/div[2]/nav/div/div[3]/button')
```