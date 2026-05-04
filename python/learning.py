import secrets
import hashlib
import base64

# Generate a random code_verifier (43-128 characters)
code_verifier = secrets.token_urlsafe(32)

# Create code_challenge using SHA-256
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode()).digest()
).decode().rstrip('=')
