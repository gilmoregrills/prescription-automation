import os

import boto3

email_body = """
<email body here>
"""


def lambda_handler(event, context):
    print(event, context)

    email = os.environ["EMAIL"]
    if "email" in event:
        email = event["email"]

    print(email)

    ses = boto3.client("ses")
    response = ses.send_email(
        Source="robin@robinyonge.com",
        Destination={
            "ToAddresses": [
                email,
            ],
            "BccAddresses": [
                "<my-email>",
            ],
        },
        Message={
            "Subject": {"Data": "Repeat Prescription"},
            "Body": {"Text": {"Data": email_body}},
        },
        ReplyToAddresses=[],
    )
    print(response)

    return {"message": "this"}
