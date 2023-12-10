import boto3
import vaultUtil import VaultClient

vault_url = "http://your-vault-server:8200"
role_id = "3c9765d5-ecf7-37b2-4fa0-c0a3006baed6"
secret_id = "0217a1ee-1fe8-9210-2572-b80f69417d36"
secret_path ="secret/data/aws"