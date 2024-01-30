#Linode Instance 

import pulumi
import pulumi_linode as linode
from dotenv import load_dotenv
import os
load_dotenv()

linode_token = os.getenv('LINODE_TOKEN')
instance_password = os.getenv('LINODE_PASSWORD')


all_types = linode.get_instance_types()
pulumi.export("typeIds", [__item.id for __item in all_types.types])

# Pulumi configuration
# pulumi_config = pulumi.Config()
# linode_token = pulumi_config.require_secret('linodeToken')

linode_provider = linode.Provider('provider', token=linode_token)

instance = linode.Instance('my-instance',
    type='g6-nanode-1',
    region='us-east',
    image='linode/ubuntu20.04',
    root_pass=instance_password,
    opts=pulumi.ResourceOptions(provider=linode_provider))

# Export the IP address of the instance
pulumi.export('ip', instance.ip_address)

