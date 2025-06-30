"""
FastMCP JWT Server
"""

from fastmcp import FastMCP
import jwt

# Configuration settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Create server
mcp = FastMCP("JWT Server")


@mcp.tool
def create_jwt(payload: dict) -> str:
    """Create a JWT token"""
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


@mcp.tool
def decode_jwt(token: str) -> dict:
    """Decode a JWT token"""
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}


@mcp.resource("jwt://create")
def jwt_create_resource() -> str:
    return "Create JWT"


@mcp.resource("jwt://decode")
def jwt_decode_resource() -> str:
    return "Decode JWT"


@mcp.prompt("jwt")
def jwt_prompt(text: str) -> str:
    return f"JWT: {text}"

