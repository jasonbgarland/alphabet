# alphabet
REST API to check if strings contains all the letters in the alphabet

# Problem Statement

You will receive a string as input, potentially a mixture of upper and lower case, numbers, special characters etc.
* The task is to determine if the string contains at least one of each letter of the alphabet.
* Return true if all are found and false if not. 
* Write it as a RESTful web service (no authentication necessary) in any language/framework you choose and
document the service.
* Please describe how you would deploy this application into AWS, including which AWS services you would use,
and what deployment method or tools.

  
# Installation

This is a pretty standard flask application. 
There are several ways to install the app locally if you want to test it.

### Python

1. Clone repo or extract the project to a directory
1. Navigate to the directory
1. Create a python virtual environment for the (arguably optional)
1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
1. Install dev dependencies if you want to run tests (optional)
    ```bash
    pip install -r requirements_dev.txt
    ```
1. Run application
    ```bash
   flask run
   ```

The endpoint will be available at http://127.0.0.1:5000/alphabet?string=<string>
The API docs can be viewed at http://127.0.0.1:5000/apidocs


# Usage

Once the server has started, online documentation can be found at: http://127.0.0.1:5000/apidocs

The endpoint is an HTTP GET endpoint. To test you can do any of the following:
* navigate to a url in the browser: example -> http://127.0.0.1:5000/alphabet?string=woof
* send a curl request to the url endpoint (remember to url encode characters as necessary)
    ```bash
    curl "http://127.0.0.1:5000/alphabet?string=the%20quick%20brown%20fox%20jumps%20over%20the%20lazy%20dog"
    ```
* use the online documentation to try out the endpoint by filling out a form -> http://127.0.0.1:5000/apidocs

# Documentation

This project has swagger API documentation setup. To access it, visit the `/apidocs` endpoint.

If running locally this would be http://127.0.0.1:5000/apidocs.

Alternatively, offline documentation for the endpoint can be found [here](chalicelib/api/docs/alphabet.md)

# Deployment


---------------


Running EC2 instance
Elastic Container Service
Elastic Beanstalk
Flask Lambda using Zappa
Flask with Lambda using serverless

However I'm going to use AWS Chalice, as it is what was used at my last job so it's the most fresh in my mind.

Note: need to find a way to update the swagger part to work with chalice 

-----

# Discussion

## Checking string

There is a more pythonic way to find out if a string contains every letter in the alphabet:

```python
import string
alphabet = string.ascii_lowercase
return set(alphabet) <= set(string_to_check.lower())
```

The lookups are very efficient, but I'm not sure that it is overall faster than the way I approached it. This is because
you still need to create a set from the string to check, which means you are processing each character in the string,
which could take awhile for very long strings. Stopping immediately when all 26 letters have been found seems 
like it would be faster.
