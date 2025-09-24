# scripts/deploy-bedrock-agent-fixed.ps1
Write-Host "🚀 Deploying Bedrock Agent Infrastructure..." -ForegroundColor Green

# Create DynamoDB table
Write-Host "📊 Creating DynamoDB table..." -ForegroundColor Yellow
python scripts/create-patient-table.py

# Deploy CDK stack
Write-Host "🏗️ Deploying CDK infrastructure..." -ForegroundColor Yellow
Set-Location infra/cdk
npm install
cdk deploy PatientLoggerStack --require-approval never
Set-Location ../..

Write-Host "✅ Deployment complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Go to AWS Console > Amazon Bedrock > Agents"
Write-Host "2. Create a new agent using the system prompt from agents/intake/system.prompt.md"
Write-Host "3. Add action group using the schema from agents/intake/tools.schema.json"
Write-Host "4. Connect to the API Gateway created by CDK"
Write-Host "5. Deploy the agent and note the Agent ID"
Write-Host "6. Update your code with the Agent ID"
Write-Host ""
Write-Host "For detailed instructions, see docs/bedrock-agent-setup.md" -ForegroundColor Blue
