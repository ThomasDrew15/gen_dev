from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
from urllib.parse import urljoin, quote

# Fill in with your personal access token and org URL
personal_access_token = 'wgkofiwfnbvt3qjxwnyseqe7tqlnkubckbmc4biwpbv55egdlj7a'
organization_url = "https://dev.azure.com/ihavenolife/"  # Note: Change to 'https' if your organization uses HTTPS
project_name = "demo"
print(organization_url)

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
print(connection)

# Get a client (the "core" client provides access to projects, teams, etc)
security_client = connection.clients.get_security_client()

# Encode the project name for URL safety
encoded_project_name = quote(project_name, safe='')
security_namespace_id = urljoin("https://dev.azure.com/ihavenolife/", encoded_project_name)
print(security_namespace_id)

# Check permissions for the specified security namespace
try:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {personal_access_token}'
    }

    response = security_client.has_permissions(security_namespace_id, headers=headers)
    print("bongo jim's crack den")

    # Iterate through permissions
    for index, permission in enumerate(response):
        pprint.pprint(f"[{index}] {permission}")

except Exception as e:
    # Handle exceptions, including redirection
    if hasattr(e, 'response') and e.response.status_code == 302:
        redirected_url = e.response.headers['Location']
        print(f"Redirected to: {redirected_url}")
    else:
        print(f"Error: {e}")
