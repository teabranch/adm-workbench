import base64
import json

def get_string_to_jwtify(header, payload):
    """
    Encodes the JWT header and payload to create the string that will be signed.

    Args:
        header (dict): A dictionary representing the JWT header.
        payload (dict): A dictionary representing the JWT payload.

    Returns:
        str: The Base64url-encoded header and payload, joined by a period.
    """

    # Serialize the header and payload dictionaries to JSON strings
    # The separators=(',', ':') argument removes whitespace for a compact representation
    json_header = json.dumps(header, separators=(',', ':')).encode('utf-8')
    json_payload = json.dumps(payload, separators=(',', ':')).encode('utf-8')

    # Base64url-encode the JSON strings
    # Standard Base64 encoding is modified for URL safety
    base64url_header = base64.urlsafe_b64encode(json_header).rstrip(b'=').decode('utf-8')
    base64url_payload = base64.urlsafe_b64encode(json_payload).rstrip(b'=').decode('utf-8')

    # The "string to jwtify" is the concatenation of the encoded header and payload
    return f"{base64url_header}.{base64url_payload}"

if __name__ == "__main__":
    # Define the JWT Header
    # 'alg' specifies the signing algorithm
    # 'typ' defines the token type as JWT
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }

    # Define the JWT Payload
    # This contains the claims, which are statements about an entity (typically, the user)
    # and additional data.
    # Registered claims like 'sub' (subject), 'name', and 'iat' (issued at) are common.
    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
    }

    # Generate the string to be signed
    string_to_sign = get_string_to_jwtify(header, payload)

    print("JWT Header:")
    print(json.dumps(header, indent=4))
    print("\nJWT Payload:")
    print(json.dumps(payload, indent=4))
    print("\n----------------------------------------\n")
    print("Base64url Encoded Header:")
    print(string_to_sign.split('.')[0])
    print("\nBase64url Encoded Payload:")
    print(string_to_sign.split('.')[1])
    print("\n----------------------------------------\n")
    print("String to be Signed (to be 'JWTified'):")
    print(string_to_sign)
    print("\nThis is the string that will be passed to the signing algorithm to create the JWT's signature.")
