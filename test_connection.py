import os
import subprocess

print("=== Environment Variables ===")
print(f"MSSQL_SERVER: {os.getenv('MSSQL_SERVER', 'Not set')}")
print(f"MSSQL_USER: {os.getenv('MSSQL_USER', 'Not set')}")
print(f"MSSQL_PASSWORD: {os.getenv('MSSQL_PASSWORD', 'Not set')}")
print(f"MSSQL_DATABASE: {os.getenv('MSSQL_DATABASE', 'Not set')}")
print()

# Get environment variables
server = os.getenv('MSSQL_SERVER')
user = os.getenv('MSSQL_USER')
password = os.getenv('MSSQL_PASSWORD')
database = os.getenv('MSSQL_DATABASE')

# Check if all required environment variables are set
if not all([server, user, password, database]):
    print("Error: Missing required environment variables!")
    print("Please set all required environment variables before running this script.")
    exit(1)

print("All environment variables are set!")
print(f"Using Server: {server}")
print(f"Using User: {user}")
print(f"Using Password: {'*' * len(password)}")
print(f"Using Database: {database}")
print()

# Change to the directory and run the command
try:
    os.chdir('/root/mssql_mcp_server')
    print("Changed to /root/mssql_mcp_server directory")
    
    # Set environment variables and run the server
    env = os.environ.copy()
    env.update({
        'MSSQL_SERVER': server,
        'MSSQL_USER': user,
        'MSSQL_PASSWORD': password,
        'MSSQL_DATABASE': database
    })
    
    print("Starting MSSQL MCP Server...")
    subprocess.run(['/root/.local/bin/uv', 'run', 'mssql_mcp_server'], env=env)
    
except Exception as e:
    print(f"Error: {e}")