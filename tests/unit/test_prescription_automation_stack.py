import aws_cdk as core
import aws_cdk.assertions as assertions

from prescription_automation.prescription_automation_stack import PrescriptionAutomationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in prescription_automation/prescription_automation_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PrescriptionAutomationStack(app, "prescription-automation")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
