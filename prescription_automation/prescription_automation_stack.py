from aws_cdk import Duration, Stack
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets
from aws_cdk import aws_iam as iam_
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_s3 as s3  # aws_sqs as sqs,
from constructs import Construct


class PrescriptionAutomationStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "prescription-automation-bucket", versioned=True)

        role = iam_.Role(
            scope=self,
            id="cdk-lambda-role",
            assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
            role_name="prescription-automation",
            managed_policies=[
                iam_.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaVPCAccessExecutionRole"
                ),
                iam_.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                ),
                iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonSESFullAccess"),
            ],
        )

        fn = lambda_.Function(
            self,
            "prescription-automation-lambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("resources"),
            handler="prescription-automation.lambda_handler",
            role=role,
            environment=dict(BUCKET=bucket.bucket_name, EMAIL="<gp email>"),
        )

        rate_trigger = events.Rule(
            self,
            "prescription-automation-trigger",
            schedule=events.Schedule.rate(Duration.days(27)),
        )
        rate_trigger.add_target(targets.LambdaFunction(fn))

        one_time_trigger = events.Rule(
            self,
            "prescription-automation-one-time-trigger",
            schedule=events.Schedule.cron(
                minute="15", hour="14", day="12", month="4", year="2023"
            ),
        )
        one_time_trigger.add_target(targets.LambdaFunction(fn))
