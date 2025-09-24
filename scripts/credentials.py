# scripts/test_env_credentials.py
import os
import boto3
import sys

def test_environment_variables():
    """Test if environment variables are set"""
    print(" Checking environment variables...")
    
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region = os.getenv('AWS_DEFAULT_REGION')
    
    print(f"AWS_ACCESS_KEY_ID: {'✅ Set' if access_key else '❌ Not set'}")
    print(f"AWS_SECRET_ACCESS_KEY: {'✅ Set' if secret_key else '❌ Not set'}")
    print(f"AWS_DEFAULT_REGION: {'✅ Set' if region else '❌ Not set'}")
    
    if not access_key or not secret_key:
        print("\n❌ Missing required environment variables!")
        return False
    
    return True

def test_credentials():
    """Test AWS credentials"""
    try:
        # Test STS
        sts_client = boto3.client('sts')
        identity = sts_client.get_caller_identity()
        print("✅ Credentials are valid!")
        print(f"Account: {identity['Account']}")
        print(f"User ID: {identity['UserId']}")
        print(f"ARN: {identity['Arn']}")
        return True
    except Exception as e:
        print(f"❌ Credentials are invalid: {e}")
        return False

def test_dynamodb():
    """Test DynamoDB access"""
    try:
        region = os.getenv('AWS_DEFAULT_REGION', 'ca-central-1')
        dynamodb = boto3.client('dynamodb', region_name=region)
        tables = dynamodb.list_tables()
        print("✅ DynamoDB access works!")
        print(f"Tables: {tables['TableNames']}")
        return True
    except Exception as e:
        print(f"❌ DynamoDB access failed: {e}")
        return False

if __name__ == "__main__":
    print(" Testing AWS Environment and Credentials")
    print("=" * 50)
    
    if test_environment_variables():
        if test_credentials():
            test_dynamodb()
    else:
        print("\n🔧 To fix this:")
        print("1. Set environment variables in PowerShell:")
        print("   $env:AWS_ACCESS_KEY_ID = 'your-access-key'")
        print("   $env:AWS_SECRET_ACCESS_KEY = 'your-secret-key'")
        print("   $env:AWS_DEFAULT_REGION = 'ca-central-1'")
        print("2. Then run this script again")