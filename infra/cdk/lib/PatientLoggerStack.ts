import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';

export class PatientLoggerStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create DynamoDB table
    const table = new dynamodb.Table(this, 'PatientInformation', {
      partitionKey: { name: 'patient_id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.RETAIN
    });

    // Create Lambda function
    const patientLogger = new lambda.Function(this, 'PatientLoggerLambda', {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: 'handler.lambda_handler',
      code: lambda.Code.fromAsset('services/patient-logger/src'),
      environment: {
        TABLE_NAME: table.tableName
      }
    });

    // Grant Lambda permissions to DynamoDB
    table.grantReadWriteData(patientLogger);
  }
}