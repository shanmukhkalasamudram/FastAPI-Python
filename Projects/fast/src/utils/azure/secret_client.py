import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

class AzureSecretsClient:
    def __init__(self, vault_url):
        self.vault_url = vault_url
        self.client = SecretClient(vault_url=self.vault_url, 
                                    credential=DefaultAzureCredential()
                                )

    def get_secret(self, key):
        secret = self.client.get_secret(key)
        return secret.value
