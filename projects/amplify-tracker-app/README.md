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

| Technology         | Description                        |
|--------------------|----------------------------------|
| React              | Frontend framework               |
| GraphQL            | API layer via AWS AppSync        |
| AWS Amplify        | Backend services and hosting     |
| Amazon Cognito     | Authentication and user management |
| Amazon DynamoDB    | NoSQL database                   |
| GitHub             | Source control and CI/CD         |
| Amazon S3          | Static file hosting              |
| AWS Lambda         | Backend logic (serverless)       |
| API Gateway        | Communication layer with Lambda  |
| Visual Studio Code | Development environment          |

---

## Getting Started

# 1. Clone the repository
git clone https://github.com/Deuche-IT/Muhlenberg.git
cd Muhlenberg

# 2. Install dependencies
npm install

# 3. Start the development server
npm run dev

# 4. Connect to Amplify backend
amplify pull --appId YOUR_APP_ID --envName dev

---

## Project Structure

.amplify/                # Internal configuration and data for Amplify CLI  
amplify/                 # Amplify backend resources (API, Auth, etc.)  
node_modules/            # Installed npm dependencies  
public/                  # Public static files (index.html, assets)  
src/                     # React and Vite source code (components, styles)  
.eslintrc                # ESLint configuration file for code linting  
.gitignore               # Files and folders ignored by Git  
amplify.yml              # Deployment configuration for Amplify Console  
amplify_outputs.json     # Backend deployment outputs and states  
CODE_OF_CONDUCT.md       # Project code of conduct  
CONTRIBUTING.md          # Contribution guidelines  
index.html               # Main public HTML file  
LICENSE                  # Project license  
package.json             # npm project metadata and scripts  
package-lock.json        # Exact versions of installed dependencies  
README.md                # Project documentation  
tsconfig.json            # TypeScript configuration for the project  
tsconfig.node.json       # TypeScript configuration for Node environment  
vite.config.ts           # Vite build tool configuration  

---

## AWS Services Used

- AWS Amplify  
- AWS Lambda  
- Amazon Cognito  
- Amazon DynamoDB  
- Amazon S3  
- API Gateway  

---

## Author

Germán Mühlenberg  
Email: gmuhlenberg@gmail.com  
GitHub: [Deuche-IT](https://github.com/Deuche-IT)
