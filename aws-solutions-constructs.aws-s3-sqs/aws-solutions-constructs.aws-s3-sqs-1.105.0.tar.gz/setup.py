import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-solutions-constructs.aws-s3-sqs",
    "version": "1.105.0",
    "description": "CDK constructs for defining an interaction between an Amazon S3 bucket and an Amazon SQS queue.",
    "license": "Apache-2.0",
    "url": "https://github.com/awslabs/aws-solutions-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-solutions-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_solutions_constructs.aws_s3_sqs",
        "aws_solutions_constructs.aws_s3_sqs._jsii"
    ],
    "package_data": {
        "aws_solutions_constructs.aws_s3_sqs._jsii": [
            "aws-s3-sqs@1.105.0.jsii.tgz"
        ],
        "aws_solutions_constructs.aws_s3_sqs": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-iam==1.105.0",
        "aws-cdk.aws-kms==1.105.0",
        "aws-cdk.aws-lambda==1.105.0",
        "aws-cdk.aws-s3-notifications==1.105.0",
        "aws-cdk.aws-s3==1.105.0",
        "aws-cdk.aws-sqs==1.105.0",
        "aws-cdk.core==1.105.0",
        "aws-solutions-constructs.core==1.105.0",
        "constructs>=3.2.0, <4.0.0",
        "jsii>=1.30.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
