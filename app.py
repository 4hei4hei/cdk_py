#!/usr/bin/env python3

from aws_cdk import core

from cdk_py.cdk_py_stack import CdkpyStack


app = core.App()
CdkpyStack(app, "cdk-py")

app.synth()
