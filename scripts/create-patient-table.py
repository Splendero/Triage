import boto3
import sys
import os
from pathlib import Path

# Add the packages directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent / 'packages'))

from pycore.src.pycore.config import BedrockConfig

def create_patient_table():
    """Create the PatientInformation DynamoDB table"""
    try:
        # Load configuration
        config = BedrockConfig()
        region = config.get_region()
        table_name = config.get_table_name()
        
        print(f"Creating table '{table_name}' in region '{region}'...")
        
        # Initialize DynamoDB with the configured region
        dynamodb = boto3.resource('dynamodb', region_name=region)
        
        # Check if table already exists
        try:
            table = dynamodb.Table(table_name)
            table.load()
            print(f"Table '{table_name}' already exists!")
            return table
        except dynamodb.meta.client.exceptions.ResourceNotFoundException:
            pass
        
        # Create the table
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'patient_id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'patient_id',
                    'AttributeType': 'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        
        # Wait for table to be created
        print("Creating table...")
        table.wait_until_exists()
        print(f"Table '{table_name}' created successfully!")
        return table
        
    except Exception as e:
        print(f"Error creating table: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure AWS CLI is configured: aws configure")
        print("2. Check your AWS credentials: aws sts get-caller-identity")
        print("3. Verify the region is correct in config/bedrock-config.json")
        sys.exit(1)

if __name__ == "__main__":
    create_patient_table()
