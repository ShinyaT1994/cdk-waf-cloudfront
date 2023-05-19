#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_waf_cloudfront.cloudfront import CloudFrontStack
from cdk_waf_cloudfront.cross_region_reference import CrossRegionReferenceStack
from cdk_waf_cloudfront.wafv2 import Wafv2Stack

app = cdk.App()

# ScopeをCloudFrontとするため、us-east-1にStackを作成する
wafv2_stack = Wafv2Stack(
    app, 'Wafv2Stack', env=cdk.Environment(region='us-east-1')
)

# us-east-1のWAFV2とap-northeast-1のCloudFrontを繋ぐためのStack
cross_region_reference_stack = CrossRegionReferenceStack(
    app, 'CrossRegionReferenceStack', wafv2_stack,
    env=cdk.Environment(region='ap-northeast-1')
)

# ap-northeast-1のStackでCloudFrontを作成する
cloudfront_stack = CloudFrontStack(
    app, 'CloudFrontStack', cross_region_reference_stack.webacl_arn,
    env=cdk.Environment(region='ap-northeast-1')
)

app.synth()
