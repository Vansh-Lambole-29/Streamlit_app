import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Read AWS credentials from dotenv file
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')

# Initialize the Bedrock Runtime client
client = boto3.client('bedrock-runtime',
                      region_name=aws_region,
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)

# Set the model ID.
model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'


# Format the request payload using the model's native structure.
def bot_response(messages):
    """It will take user prompt as input and return the response from the model

    This function is used to invoke the model and get the response for the given prompt.

    Args:
        prompt (str): prompt to be passed to the model

    Returns:
        str: response from the model
    """
    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.1,
        "top_p": 0.96,
        "messages": messages
    }

    # Convert the native request to JSON.
    request = json.dumps(native_request)

    # Invoke the model with the request.
    response = client.invoke_model(modelId=model_id, body=request)

    # Decode the response body.
    model_response = json.loads(response["body"].read())

    # Extract and print the response text.
    response_text = model_response["content"][0]["text"]
    # print(response_text, type(response_text))
    return response_text
