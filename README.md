# BrokenLink
### Description

This is a simple but advanced script that can find broken links and a few other things from a URL.

This script was last tested on Python version 3.11.2

## Setup

1. Install the required modules:

   ```bash
   pip install requests tldextract beautifulsoup4 colorama
   ```

2. Run the script:

   ```bash
   python script.py
   ```

   or

   ```bash
   python3 script.py
   ```

   If you do not want to use command line arguments, the script will prompt you to enter the URL.

## Results

The script checks the links on the main URL page and displays the total number of links, broken links, links that redirect to another address, and links with errors.

Sample output:

```
Total URLs: 100 Links; 5 Broken links; 3 Redirect link; 2 Error
[Broken] https://example.com/link1
[Broken] https://example.com/link2
[Redirect] https://redirected-link.com
[Error] https://example.com/link3

...
```

Please note that this README.md file is just an example and you can modify it according to your needs.
