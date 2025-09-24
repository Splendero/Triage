# Medical Intake Agent

> 🏆 Built for the AWS AI Agent Hackathon - September 2025

A Bedrock-powered medical intake system that demonstrates the power of AWS Agents in healthcare automation. This project showcases how AI agents can streamline patient information gathering while maintaining a natural, conversational experience.

## 🎯 Hackathon Focus

This project explores the potential of AWS Bedrock Agents in healthcare by:
- Creating a conversational AI intake system
- Demonstrating secure patient data handling
- Showcasing agent-to-database integration
- Implementing best practices for medical data collection

## ✨ Key Features

- Natural conversation flow using Claude 3 Sonnet
- Secure patient data storage in DynamoDB
- Step-by-step information gathering
- Confirmation-based data saving
- HIPAA-conscious design patterns

## 🏗️ Project Structure

```
├── agents/
│   └── intake/
│       ├── system.prompt.md    # Agent prompt
│       └── openapi.json        # API schema
├── services/
│   └── patient-logger/
│       ├── src/
│       │   └── handler.py      # Lambda handler
│       └── requirements.txt     # Python dependencies
└── infra/
    └── cdk/                    # Infrastructure code
```


## ⚙️ AWS Services Used

- **Amazon Bedrock**: Powers the conversational AI agent
- **AWS Lambda**: Handles data processing and storage
- **Amazon DynamoDB**: Secures patient information
- **AWS IAM**: Manages service permissions

## 🔒 Security & Compliance

- All patient data is stored securely in DynamoDB
- Lambda function uses least-privilege permissions
- Environment variables for sensitive configuration
- Design considers HIPAA compliance patterns

## 🌟 Hackathon Implementation

This project demonstrates several key aspects of AWS Agent capabilities:
1. **Natural Language Processing**: Using Claude 3 Sonnet for human-like interaction
2. **Structured Data Collection**: Converting conversations to structured database entries
3. **Confirmation Workflow**: Ensuring data accuracy through user confirmation
4. **Error Handling**: Graceful handling of various user inputs and edge cases

## 🤝 Contributing

This project was created for the AWS AI Agent Hackathon but welcomes contributions! Feel free to:
- Submit issues
- Propose new features
- Send pull requests

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- AWS AI Agent Hackathon organizers and mentors
- The AWS Bedrock and Claude teams
- Healthcare professionals who provided domain insights
