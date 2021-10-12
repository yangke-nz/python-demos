import hmac
import hashlib

SECRET = 'the-secret'
payload = '{"ref":"refs/heads/main"}'
signature = hmac.new(bytes(SECRET, 'utf-8'), msg = bytes(payload , 'utf-8'), digestmod = hashlib.sha256).hexdigest()
print(signature)
