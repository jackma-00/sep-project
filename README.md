# Swedish Event Planning Business Project

This repository contains the backend of the SEP project. 

## Requirements

* Docker engine ([Installation](https://docs.docker.com/engine/install/))
* Python3.10.12 with `pip`

## Quickstart for development experiments 

First, get valid AWS credentials with enough permissions to create and deploy Cloudformation stacks.

The deployment configuration (AWS account and AWS region) is hard-coded into the `mlops-ai-engine.ts` deployment file.

Run the make target `install` to install all the npm's dependencies
```shell
make install
```

### Python venv

Step into `assets/ai-engine/` directory and initialize the Python environment 
**Note:** your Python3 version has to be 3.10.6 in order to assure Lambda function's support
```shell
python3 -m venv .venv
. .venv/bin/activate
```

Install now the Python project's dependencies running the make target
```shell
make install
```

### Test Build Deploy

To develop new features, test and deploy them consult the [specific documentation](https://github.com/giacomowisee/mlops-ai-engine/blob/main/assets/ai-engine/README.md#development).

### Lambda function testing

Once the development Lambda function is updated with the new features you can both:
* visit its URL and post the [sample input request](https://github.com/giacomowisee/mlops-ai-engine/blob/main/assets/ai-engine/app/sample-data/input42.json) on the end-point `docs/`.
* or do the same but using Postman. 

## Production 

Thanks to the GitHub workflows the code will be automatically tested, built and deployed to the production environment specified in the files themselves as well as GitHub secrets. 

Particularly, the assets' code will be tested while making pull requests to the base GitHub repository. On success of those tests the application and subsequently the Lambda function will be deployed into production. 

**Note:** while testing, the github workflow _prd-test.yml_ will test AI Engine invoking the development AI model. If we want to test AI Engine against the production AI model first we need to deploy it, secondly we must overwrite the testing workflow _lambda-models_ variable targeting that model.