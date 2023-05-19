from constructs import Construct
from cdk_remote_stack import RemoteOutputs
from aws_cdk import (
    Stack,
)


class CrossRegionReferenceStack(Stack):
    
    @property
    def webacl_id(self):
        return self.__webacl_id
    
    def __init__(
            self, scope: Construct, id: str, wafv2_stack, **kwargs
            ) -> None:
        super().__init__(scope, id, **kwargs)
        
        # 依存関係を定義
        self.add_dependency(wafv2_stack)
        
        # CloudFormation outputを取得
        cfn_outputs = RemoteOutputs(self, 'CfnOutputs', stack=wafv2_stack)
        
        # Web ACL ARN を取得
        self.webacl_arn = cfn_outputs.get('WebAclArn')