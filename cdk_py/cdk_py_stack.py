from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    core,
)

class CdkpyStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    log_bucket = s3.Bucket(self,
                          "access_log",
                          versioned = True,
                          removal_policy = core.RemovalPolicy.DESTROY,)

    web_bucket = s3.Bucket(self,
                      "web",
                      versioned = False,
                      public_read_access = True,
                      website_index_document = "index.html",
                      website_error_document = 'error.html',
                      server_access_logs_bucket = log_bucket,
                      server_access_logs_prefix = "access_",
                      removal_policy = core.RemovalPolicy.DESTROY,)
    
    deploy = s3deploy.BucketDeployment(self,
                                      "DeployWebsite",
                                      sources = [s3deploy.Source.asset("./src")],
                                      destination_bucket = web_bucket,)

