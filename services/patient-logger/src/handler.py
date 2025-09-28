import json
import boto3
from datetime import datetime
import uuid

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('PatientInformation')

REQUIRED_FIELDS = ['first_name', 'last_name', 'symptoms', 'medical_id']
OPTIONAL_FIELDS = ['date_of_birth']

def lambda_handler(event, context):
    try:
        print("=== INPUT ===")
        print("FULL BEDROCK EVENT:")
        print(json.dumps(event, indent=2))
        
        # Get values from event
        action_group = event['actionGroup']
        function = event['function']
        message_version = event.get('messageVersion', '1.0')
        session_attributes = event.get('sessionAttributes', {})
        prompt_session_attributes = event.get('promptSessionAttributes', {})
        parameters = event.get('parameters', [])

        # Extract parameters
        patient_data = {}
        for param in parameters:
            patient_data[param['name']] = param['value']
        
        # Validate required fields
        missing_fields = [field for field in REQUIRED_FIELDS if field not in patient_data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

        # Add system fields
        patient_data['patient_id'] = f"patient_{str(uuid.uuid4())}"
        patient_data['created_at'] = datetime.now().isoformat()
        
        print(f"Saving patient data: {json.dumps(patient_data)}")
        table.put_item(Item=patient_data)

        # Return exact format for function-based action groups
        return {
            "messageVersion": message_version,
            "response": {
                "actionGroup": action_group,
                "function": function,
                "functionResponse": {
                    "responseBody": {
                        "TEXT": {  # Only TEXT is supported currently
                            "body": json.dumps({
                                "success": True,
                                "message": f"Successfully logged patient: {patient_data.get('first_name', '')} {patient_data.get('last_name', '')}",
                                "patient_id": patient_data['patient_id']
                            })
                        }
                    }
                }
            },
            "sessionAttributes": session_attributes,
            "promptSessionAttributes": prompt_session_attributes
        }

    except Exception as e:
        print(f"=== ERROR ===")
        print(f"Error: {str(e)}")
        return {
            "messageVersion": "1.0",
            "response": {
                "actionGroup": action_group if 'action_group' in locals() else "patientLogging",
                "function": function if 'function' in locals() else "log-test-1",
                "functionResponse": {
                    "responseState": "FAILURE",  # Tell Bedrock this was a failure
                    "responseBody": {
                        "TEXT": {
                            "body": json.dumps({
                                "success": False,
                                "error": str(e)
                            })
                        }
                    }
                }
            },
            "sessionAttributes": session_attributes if 'session_attributes' in locals() else {},
            "promptSessionAttributes": prompt_session_attributes if 'prompt_session_attributes' in locals() else {}
        }