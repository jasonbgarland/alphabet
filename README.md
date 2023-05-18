# alphabet
REST API to check if strings contains all the letters in the alphabet.

# Problem Statement

You will receive a string as input, potentially a mixture of upper and lower case, numbers, special characters etc.
* The task is to determine if the string contains at least one of each letter of the alphabet.
* Return true if all are found and false if not. 
* Write it as a RESTful web service (no authentication necessary) in any language/framework you choose and
document the service.
* Please describe how you would deploy this application into AWS, including which AWS services you would use,
and what deployment method or tools.

  
# Installation

This project is written in [Chalice](https://aws.github.io/chalice/), which is an AWS framework for writing serverless 
applications. Chalice is very similar to the Flask framework in Python, with a few small changes.

The instructions below describe how to install locally:

1. Clone repo or extract the project to a directory
1. Navigate to the directory
1. Create a python virtual environment for the project
1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
1. Install dev dependencies if you want to run tests (optional)
    ```bash
    pip install -r requirements_dev.txt
    ```
1. Run the service in local mode if you want to start manual testing.
    ```bash
    chalice local
    ```

The endpoint will be available at http://127.0.0.1:8000/alphabet?string=<string>  
Replace the `<string>` portion at the end with the string you want to use to test it.

# Usage

The endpoint is an HTTP GET endpoint. To test you can do any of the following:
* navigate to a url in the browser: example -> http://127.0.0.1:8000/alphabet?string=woof
* send a curl request to the url endpoint (remember to url encode characters as necessary)
    ```bash
    curl "http://127.0.0.1:8000/alphabet?string=the%20quick%20brown%20fox%20jumps%20over%20the%20lazy%20dog"
    ```

# Testing

Unit and integration tests for the project can be run using `pytest`. 
Make sure to install pytest (pip install -r requirements_dev.txt) and then in the project root directory run:  
```bash
pytest -v
```

# Documentation

Documentation for the endpoint can be found [here](chalicelib/api/docs/alphabet.md)

# Deployment

### Manual

A manual deployment can be made using the chalice cli. This may or may not work on your machine, based on your AWS
cli configuration and IAM role permissions.

```bash
chalice deploy
```

Running this command creats or updates an AWS Lambda function named alphabet.

### Automated (CI/CD)

This project is hosted on my personal github at https://github.com/jasonbgarland/alphabet.  

A github action has been created that uses `.github/workflows/main.yml` as its configuration. This workflow installs 
project dependencies and runs the unit and integration tests whenever an update occurs in the repo.

For deployment, an AWS CodePipeline has been created that triggers off of github pushes to the main branch.
This is based on the configuration at `infrastructure/pipeline.json`. The pipeline does the following:

1. pull code from github
1. build and package the project (using the settings in `buildspec.yml`
1. deploy the package as a lambda function using CloudFormation

This functionality will all be demoed in the upcoming interview on 5/19.

# Discussion

## Framework

I've been using `Python` and `Flask` the most lately, so I actually wrote the solution in Flask first.  Then when I was
trying to get it to deploy to a lambda without a lot of fuss, it took me awhile to remember that for the last 3 years
I've been contributing to a repo that was using `Chalice`. It is easy to get confused because the frameworks are very
similar. But Chalice is meant to make it easy to deploy to lambda, so I refactored the project to use that since
this project isn't supposed to take a ton of time to complete.

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

## Deployment

At my last job, the framework and CI/CD hooks for deployment are what I used in this project. In researching, I realized
that there are a lot of different ways you can push your code up to AWS, including:

* Running EC2 instance
* Elastic Container Service
* Elastic Beanstalk
* Terraform
* Flask with Lambda using Zappa
* Flask with Lambda using serverless

Every organization is different and has different needs and preferences. In the past, I have setup EC2 instances
to deploy to, as well as docker containers to deploy.

## Reference

For reference, this is what I referred to in help setting up the AWS side:
https://aws.amazon.com/blogs/developer/automatically-deploy-a-serverless-rest-api-from-github-with-aws-chalice/

And this is what I referred to in help setting up the github side:
https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python
