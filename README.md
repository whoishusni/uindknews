# UIN Datokarama Palu News API (Unofficial)

This project is designed to scrape news data from the official website of **UIN Datokarama Palu** and serve it as an API. It provides an **unofficial** API endpoint to access the latest news content in a structured format.

## Project Overview

- **Purpose:** Scrape Last 9 news articles from the UIN Datokarama Palu website.
- **Output:** Provide an API to access the scraped news data.
- **Note:** This is an unofficial API and is not affiliated with UIN Datokarama Palu.

## Tech Stack

- **Python**: A versatile programming language used for data processing, web scraping, and backend services.  
- **Scrapy**: An open-source framework for web scraping, designed for large-scale crawling and data extraction.  
- **Requests**: A simple, elegant HTTP library for Python to send HTTP requests, useful for interacting with external APIs or web services.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python. It supports automatic generation of API documentation using Swagger.  
- **Pydantic**: A data validation and settings management library for Python. It validates and parses data using Python’s type annotations.


## Installation & Setup

1. **Clone the project**

   ```bash
   git clone https://github.com/whoishusni/uindknews.git
   cd uindknews

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

2. **Instal Dependency**

   ```bash
   pip3 install -r requirements.txt

## Usage

1. **Start the Scrapy Spider to Scrape News Data**  
   To scrape the latest 9 news articles from the UIN Datokarama Palu website, you can run the Scrapy spider.
   ```bash
   cd uindknews
   scrapy crawl uindknewsspider

2. **Run the FastAPI server to Serve the Data as an API**  
   To expose the scraped news data as an API, you can use FastAPI. Start the FastAPI server by running:
   ```bash
   cd uindknews/api
   uvicorn apimain:app --reload
   
3. **Stop The Server**  
   When you're done, you can stop the FastAPI server by pressing ```Ctrl + C``` in the terminal where the server is running.

## API Reference

#### API Docs

```http
  GET /api/v1/docs
```

