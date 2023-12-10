import requests

# Vault server details
vault_url = "http://your-vault-server:8200"
role_id = "3c9765d5-ecf7-37b2-4fa0-c0a3006baed6"
secret_id = "0217a1ee-1fe8-9210-2572-b80f69417d36"
secret_path ="secret/data/aws"

class getVaultCred:
    def authenticate_with_approle():
        auth_url = f"{vault_url}/v1/auth/approle/login"
        auth_data = {
            "role_id": role_id,
            "secret_id":secret_id
        }

        try:
            auth_response = requests.post(auth_url, json=auth_data)
            auth_response.raise_for_status()

            token = auth_response.json()["auth"]["client_token"]
            print("token===============",token)
            return token
        except requests.exceptions.RequestException as e:
            print(f"Authentication error: {e}")
            return None
        
    def get_secret(token):
        headers = {
            "X-Vault-Token": token,
        }

        url = f"{vault_url}/v1/{secret_path}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            secret_data = response.json()["data"]
            return secret_data
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving secret:{e}")
            return None
        
# token = authenticate_with_approle()
# secret_data = get_secret(token)
# print(secret_data)