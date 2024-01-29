#Linode Instance 

import pulumi
import pulumi_linode as linode
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

linode_token = os.getenv('LINODE_TOKEN')
instance_password = os.getenv('LINODE_PASSWORD')

# Replace 'your_linode_token' with your actual Linode token.
# It's recommended to use Pulumi configuration or environment variables for tokens, not hardcoding
# pulumi_config = pulumi.Config()
# linode_token = pulumi_config.require_secret('linodeToken')

# Configure the Linode provider with the provided token
linode_provider = linode.Provider('provider', token=linode_token)

# Define a Linode instance with the required properties
instance = linode.Instance('my-instance',
    type='g6-nanode-1', # This is a type of instance, replace with your desired type
    region='us-east',   # Replace with your desired region
    image='linode/ubuntu20.04', # Replace with your desired image
    root_pass=instance_password, # Replace with your desired root password
    opts=pulumi.ResourceOptions(provider=linode_provider))

# Export the IP address of the instance
pulumi.export('ip', instance.ip_address)

