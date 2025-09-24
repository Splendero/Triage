import * as cdk from 'aws-cdk-lib';
import { PatientLoggerStack } from '../lib/PatientLoggerStack';

const app = new cdk.App();

new PatientLoggerStack(app, 'PatientLoggerStack', {
  env: {
    account: '233573279515',  // Your account ID
    region: 'ca-central-1'
  }
});
