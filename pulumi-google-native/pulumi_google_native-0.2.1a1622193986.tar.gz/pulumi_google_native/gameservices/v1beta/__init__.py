# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .game_server_deployment import *
from .game_server_deployment_config import *
from .game_server_deployment_iam_policy import *
from .realm import *
from .realm_game_server_cluster import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "google-native:gameservices/v1beta:GameServerDeployment":
                return GameServerDeployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:gameservices/v1beta:GameServerDeploymentConfig":
                return GameServerDeploymentConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:gameservices/v1beta:GameServerDeploymentIamPolicy":
                return GameServerDeploymentIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:gameservices/v1beta:Realm":
                return Realm(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "google-native:gameservices/v1beta:RealmGameServerCluster":
                return RealmGameServerCluster(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("google-native", "gameservices/v1beta", _module_instance)

_register_module()
