# Purpose

This project is designed to automatically adjust the minimum value of an ECS task at regular intervals. The goal is to maintain the optimal level of resources needed to run the task effectively.

# Environment

## Infrastructure
- Event-Bridge: A serverless event bus that makes it easy to connect different AWS services together.
- Lambda: An AWS service that allows you to run code in the cloud without having to manage any infrastructure.

## Programming Languages
- Serverless.js: A framework that makes it easy to develop, deploy, and manage serverless applications.
- Python: A high-level programming language that is widely used in scientific computing, data analysis, and artificial intelligence applications.

# How to Run

1. Install serverless.js globally on your system by running the following command in your terminal:

```
npm install -g serverless
```

2. Install the required node modules by running the following command in the project directory:
```
npm install
```

3. Deploy the application by running the following command in the project directory:
```
serverless deploy
```

# Environment Variables
- slackToken: A Slack API token used to receive notifications about the status of the adjustment process.
- clusterName: The name of the ECS cluster where the task is running.
- serviceName: The name of the ECS service that is running the task.


