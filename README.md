# Research Paper RSS2 Web Scraper
This Python program is able to retrieve research paper entries from university RSS feeds.

## Requirements
- The RSS2 URL must have a query parameter that allows you to specify a keyword
- Python 3.7.7+
- feedparser
- pandas

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries
```sh
pip install -r requirements.txt
```

## Usage
The keywords.txt file contains all the keywords that the web scraper searches for. You can alter this to your preference.

You can execute the following command on terminal to run the program:
```sh
python main.py
```
When the program runs it will first prompt you to enter the RSS feed URL:
```sh
Please enter the RSS feed URL: 
```
You need to provide the RSS feed URL and specify the keyword field by putting [keyword]:
```sh
http://university.com/rssfeed2.xml?keywords=[keyword]
```
It will then prompt for the university name which will is used to name the CSV output file.

The CSV file output file will have the columns: title, link, description, keyword, university.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Licence
[MIT](LICENSE)