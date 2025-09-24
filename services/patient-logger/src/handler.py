import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    try:
        # Print the incoming event for debugging
        print("Received event:", json.dumps(event))
        
        # Extract parameters from the request body
        try:
            # First try to parse from requestBody if it exists
            if 'requestBody' in event:
                body = json.loads(event['requestBody'])
                first_name = body.get('first_name', '')
                last_name = body.get('last_name', '')
            # Fallback to parameters if requestBody doesn't exist
            else:
                parameters = event.get('parameters', {})
                first_name = parameters.get('first_name', '')
                last_name = parameters.get('last_name', '')
        except json.JSONDecodeError:
            print("Error decoding request body")
            first_name = ''
            last_name = ''
        
        print(f"Extracted names: first_name='{first_name}', last_name='{last_name}'")
        
        # Generate patient ID
        patient_id = f"patient_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Create patient data
        patient_data = {
            'patient_id': patient_id,
            'first_name': first_name,
            'last_name': last_name,
            'created_at': datetime.now().isoformat()
        }
        
        # Initialize DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('PatientInformation')
        
        # Save to DynamoDB
        table.put_item(Item=patient_data)
        print(f"Saved to DynamoDB: {json.dumps(patient_data)}")
        
        # Create response in the format AgentCore expects
        response = {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": "patient-data-actions",
                "apiPath": "/patient",
                "httpMethod": "POST",
                "httpStatusCode": 200,
                "responseBody": json.dumps({
                    "success": True,
                    "message": f"Successfully logged patient: {first_name} {last_name}",
                    "patient_id": patient_id
                })
            }
        }
        
        print("Sending response:", json.dumps(response))
        return response
        
    except Exception as e:
        print("Error:", str(e))
        error_response = {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": "patient-data-actions",
                "apiPath": "/patient",
                "httpMethod": "POST",
                "httpStatusCode": 500,
                "responseBody": json.dumps({
                    "success": False,
                    "error": str(e)
                })
            }
        }
        print("Sending error response:", json.dumps(error_response))
        return error_response
