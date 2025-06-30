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

    json_header = json.dumps(header, separators=(',', ':')).encode('utf-8')
    json_payload = json.dumps(payload, separators=(',', ':')).encode('utf-8')

    base64url_header = base64.urlsafe_b64encode(json_header).rstrip(b'=').decode('utf-8')
    base64url_payload = base64.urlsafe_b64encode(json_payload).rstrip(b'=').decode('utf-8')

    return f"{base64url_header}.{base64url_payload}"

