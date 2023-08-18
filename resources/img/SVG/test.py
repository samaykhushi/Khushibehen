
import requests
import base64

def upload_file_to_github(access_token, repo_owner, repo_name, local_file_path, branch_name, commit_message):
   
    base_url = "https://api.github.com"

   
    headers = {
        "Authorization": f"token {access_token}"
    }

  
    with open(local_file_path, "rb") as file:
        content = file.read()
        encoded_content = base64.b64encode(content).decode()

    file_url = f"{base_url}/repos/{repo_owner}/{repo_name}/contents/resources/img/SVG/{local_file_path}"


    payload = {
        "message": commit_message,
        "content": encoded_content,
        "branch": branch_name,
    }


    response = requests.put(file_url, headers=headers, json=payload)

    if response.status_code == 201:
        pass
       
    else:
        print('Failed !!')


access_token = "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"
repo_name = 'license'
repo_owner = 'samaykhushi'
local_file_path = 'license.conf'  
branch_name = 'main'  
commit_message = 'Upload file'  
           
upload_file_to_github(access_token, repo_owner,repo_name, local_file_path, branch_name, commit_message)
