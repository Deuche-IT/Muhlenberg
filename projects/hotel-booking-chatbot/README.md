# Hotel Booking Chatbot

<img src="./assets/chatbot.gif" alt="Demo Amplify Tracker" width="600"/>

## Project Overview
This chatbot was developed using Amazon Lex to manage hotel bookings, with AWS Lambda handling the intent logic and Amazon Translate providing multilingual support.

## Technologies Used
- **Amazon Lex** – Conversational interface for hotel booking.
- **AWS Lambda** (Python) – Processes the intent logic and slot management.
- **Amazon Translate** – Translates user inputs dynamically to support multiple languages.
- **Amazon CloudWatch Logs** – Monitors and debugs intent events and input values.
- **IAM, AWS CLI** – Used for manual permission and credential configuration if needed.

## Functionality
- **Main Intent:** `BookHotel`, with slots like:
  - `Location`
  - `CheckInDate`
  - `Nights`
  - `RoomType`
- Progressive slot elicitation using `DialogCodeHook`.
- Automatic translation of user inputs in different languages.
- CloudWatch used for debugging and validating Lex's interpreted values (e.g., converting `"3"` into a date like `"2026-03-01"`).
- Dynamic conversational flow depending on user state and slot completion.

## Possible Enhancements
- Add email/SMS confirmation using Amazon SNS.
- Integrate with a hotel API or DynamoDB to manage real availability.
- Improve error handling and fallback strategies.
