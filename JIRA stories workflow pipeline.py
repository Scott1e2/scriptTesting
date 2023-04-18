#try to move other user stories to my workflow
from jira import JIRA
import json

# Connect to the JIRA instance containing the stories to import
jira_src = JIRA(basic_auth=("username", "password"), options={"server": "https://jira.example.com"})

# Connect to the JIRA instance to import the stories to
jira_dest = JIRA(basic_auth=("username", "password"), options={"server": "https://jira.example.com"})

# Get the stories to import
issues_src = jira_src.search_issues("project=PROJECT_NAME", maxResults=1000)

# Iterate through the stories
for issue in issues_src:
    # Get the JSON representation of the issue
    issue_json = json.loads(issue.raw)

    # Remove unwanted fields from the JSON
    del issue_json["fields"]["components"]
    del issue_json["fields"]["customfield_12345"]

    # Create the issue in the destination JIRA instance
    new_issue = jira_dest.create_issue(fields=issue_json["fields"])

print("Import complete!")

#This script connects to two JIRA instances, one containing the stories to import, and one to import the stories to. It then uses the JIRA search function to retrieve the stories to import, and iterates through them, creating a new issue in the destination JIRA instance for each one.

#You will need to replace "username" and "password" with the appropriate credentials to connect to the JIRA instances, and "https://jira.example.com" with the correct URL of your JIRA instances. Also, replace the "project=PROJECT_NAME" with the name of the project you want to import stories from.

#You also need to install jira library by running !pip install jira

