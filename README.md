# BubbleAPI Python Wrapper

## Description

The `BubbleAPI` Python class provides a convenient wrapper around the Bubble API, allowing for easy interaction with the Bubble application platform through Python. It supports various HTTP methods including GET, POST, PUT, and DELETE, handling authentication and requests seamlessly.

## Installation

To use the `BubbleAPI` class, you must have Python and the `requests` library installed on your system.

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).
2. **Install `requests` library**: Use pip to install the `requests` library.

    ```bash
    pip install requests
    ```

## Usage

### Setup

First, import the `BubbleAPI` class from your script and initialize it with your base URL and token.

```python
from your_module_name import BubbleAPI

api = BubbleAPI(base_url='https://yourbubbleapp.bubbleapps.io/version-test/api/1.1/', token='your_token_here')
```
### Making a GET Request

To retrieve data from your Bubble application:

```python
response = api.get(endpoint='your_endpoint')
print(response)
```

### Making a POST Request

To create new data in your Bubble application:

```python

data = {"key": "value"}  # your data here
response = api.post(endpoint='your_endpoint', json=data)
print(response)
```