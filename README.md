# BrokenLink
### Description

This script checks for broken and redirected links on a given webpage. It retrieves all the URLs from the webpage, follows any redirects, and checks the response status code for each URL. The script outputs the total number of URLs, the number of broken links, the number of redirected links, and any errors encountered during the process.
Requirements

Built on Python version 3.11.2

### Installation

Clone the repository:

```shell
git clone https://github.com/MrRajabZade/BrokenLink/
```

Install the required libraries:

```shell
python -m pip install -r requirements.txt
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
