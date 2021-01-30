from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    core,
)

class CdkpyStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    bucket = s3.Bucket(self,
                      "web",
                      versioned = False,
                      public_read_access = True,
                      website_index_document="index.html",
                      removal_policy = core.RemovalPolicy.DESTROY,)
    
    deploy = s3deploy.BucketDeployment(self,
                                      "DeployWebsite",
                                      sources = [s3deploy.Source.asset("./src")],
                                      destination_key_prefix="web/",
                                      #server_side_encryption=ServerSideEncryption.AES_256,
                                      destination_bucket = bucket,)

