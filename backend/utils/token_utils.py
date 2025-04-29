import base64

def get_basic_auth_header(client_id, client_secret):
  auth_str = f'{client_id}:{client_secret}'
  auth_bytes = auth_str.encode('utf-8')
  auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
  return f'Basic {auth_b64}'