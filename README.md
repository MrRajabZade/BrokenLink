# BrokenLink
### Description

This script checks for broken and redirected links on a given webpage. It retrieves all the URLs from the webpage, follows any redirects, and checks the response status code for each URL. The script outputs the total number of URLs, the number of broken links, the number of redirected links, and any errors encountered during the process.
Requirements

- Python 3.x
- requests library
- bs4 (BeautifulSoup) library
- tldextract library
- rich library

### Installation

Clone the repository:

```shell
git clone https://github.com/MrRajabZade/BrokenLink/
```

Install the required libraries:

```shell
pip install requests bs4 tldextract rich
```

### Usage

Open a terminal and navigate to the cloned repository's directory.

Run the script using the following command:

```shell
python main.py [URL]
```

Replace [URL] with the URL of the webpage you want to check. If no URL is provided as a command-line argument, the script will prompt you to enter a URL during runtime.

Wait for the script to finish. It will display a progress bar indicating the status of the link checks.

Once the script completes, it will generate a file named "Result.txt" in the same directory. This file will contain the broken links, redirected links, and any errors encountered.

### Example

```shell
python main.py https://example.com
```

### Notes

- The script uses the ```get_domain()``` function from the ```tldextract``` library to extract the domain from a URL.
- The ```get_redirected_site()``` function checks for redirects and returns the redirected site's domain if applicable.
- The ```check()``` function checks the response status code for a given link and compares it with the domain. It returns different codes based on the result.
- The ```find_urls()``` function retrieves all the URLs from a webpage using BeautifulSoup.
- The script uses the ```Progress``` class from the ```rich``` library to display a progress bar during link checks.
