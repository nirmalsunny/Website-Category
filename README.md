# Website-Category
Pulls data from sitereview service.

### Description

Site Review described by Symantec:

*"Site Review allows users to check and dispute the current WebPulse categorization for any URL"*

https://sitereview.bluecoat.com/

This Python script allows Users to quickly query the Site Review service via the CLI. This script can be run stand-alone, or imported as a module to extend the functionality of another script.

### Usage

website_category.py takes one mandatory positional argument, url, and submits it to the Site Review service:

```
usage: website_category.py url

```

### Results

Test Result for facebook.com:

```
==================
Website Category
==================

URL: facebook.com
Category: Social Networking
```
### Installation

geckodriver is required. The path of geckodriver needs to be edited.

### Python Requirements

* selenium

