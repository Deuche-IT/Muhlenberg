# React To-Do App with AWS Amplify Gen 2

A full-stack To-Do List Application built with React, using AWS Amplify Gen 2 for the backend and Amazon DynamoDB for data persistence. Includes user authentication, real-time updates, and CI/CD through GitHub.

---

## Features

- Create, view, and delete tasks
- User authentication with Amazon Cognito
- Serverless functions using AWS Lambda
- Data storage with Amazon DynamoDB
- Static asset hosting via Amazon S3
- Backend integration through AWS API Gateway
- Real-time updates using GraphQL subscriptions
- Continuous deployment with Amplify Hosting
- Git-based CI/CD using GitHub

---

## Tech Stack

| Technology      | Description                        |
|------------------|------------------------------------|
| React           | Frontend framework                 |
| GraphQL         | API layer via AWS AppSync          |
| AWS Amplify     | Backend services and hosting       |
| Amazon Cognito  | Authentication and user management |
| Amazon DynamoDB | NoSQL database                     |
| GitHub          | Source control and CI/CD           |
| Amazon S3       | Static file hosting                |
| AWS Lambda      | Backend logic (serverless)         |
| API Gateway     | Communication layer with Lambda    |
| Visual Studio Code | Development environment         |

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# 2. Install dependencies
npm install

# 3. Start the development server
npm run dev

# 4. Connect to Amplify backend
amplify pull --appId YOUR_APP_ID --envName dev
