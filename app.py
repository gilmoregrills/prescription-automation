#!/usr/bin/env python3
import os

import aws_cdk as cdk

from prescription_automation.prescription_automation_stack import PrescriptionAutomationStack


app = cdk.App()
PrescriptionAutomationStack(app, "PrescriptionAutomationStack", 
                            env=cdk.Environment(
                                account='553762194992', 
                                region='eu-west-2'
                            ),
    )

app.synth()
