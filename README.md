# IMDb Web Scraper using Streamlit

This project demonstrates a simple web scraping application built with Python, Streamlit, `requests`, and `BeautifulSoup` libraries to extract information from IMDb movie pages based on user-provided IMDb Movie IDs.

## Project Overview

The purpose of this project is to showcase how to use web scraping techniques to fetch movie information from IMDb using the provided IMDb Movie ID. The extracted data includes movie title, rating, and description.

## How to Run

1. Make sure you have Python and the required libraries installed (Streamlit, `requests`, and `BeautifulSoup`). You can install them using the following commands:

```bash
pip install streamlit requests beautifulsoup4
```

2. Create a new Python file (e.g., `imdb_scraper.py`) and copy the provided code into it.

3. Open a terminal and navigate to the directory containing the `imdb_scraper.py` file.

4. Run the Streamlit app using the following command:

```bash
streamlit run imdb_scraper.py
```

5. The Streamlit app will open in a web browser. Enter a valid IMDb Movie ID (e.g., `tt0468569`) and click "Enter."

## Learning Objectives

By working on this project, I have learned the following concepts:

- **Web Scraping**: You learned how to send HTTP requests to web pages using the `requests` library and how to parse HTML content using `BeautifulSoup`.

- **User Interaction with Streamlit**: You explored how to create a simple interactive web application using Streamlit. Users can input IMDb Movie IDs, and the app responds by displaying relevant movie information.

- **Data Extraction**: You practiced locating specific elements within a webpage using their class names and extracting the desired data. The project covers extracting movie titles, ratings, and descriptions.

- **Error Handling**: The project includes basic error handling to deal with scenarios such as invalid IMDb Movie IDs.

- **Web Page Structure**: Through this project, you gained insights into the structure of IMDb movie pages and learned how to identify HTML elements for extracting desired information.

## Considerations

- **Website Changes**: Keep in mind that websites' structures may change over time, potentially affecting the code's functionality. Regularly inspect the HTML structure and class names to ensure accurate scraping.

- **Ethical Use**: Always respect the terms of use and guidelines of websites when scraping data. Avoid overloading their servers with excessive requests and ensure your scraping activities are legal and ethical.

- **Continuous Learning**: Web scraping is a powerful skill, and this project serves as a starting point. Consider exploring more advanced techniques such as handling dynamic websites, pagination, and handling asynchronous requests.

Remember that this project offers a foundational understanding of web scraping and interactive app development. Continue to expand your skills and apply them to various real-world scenarios.
