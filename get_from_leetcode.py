import time
import requests

def get_session_info():

    with open('session_info.txt', 'r') as file:
        session_id = file.readline().strip()
        csrftoken = file.readline().strip()

    session_info = {
        "session_id": session_id.split(':')[1].replace('"', ''),
        "csrftoken": csrftoken.split(':')[1].replace('"','')
    }


    return session_info


# LeetCode GraphQL API URL
URL = "https://leetcode.com/graphql"

# GraphQL Query to fetch recent submissions
GRAPHQL_QUERY = """
query userSubmissionList($username: String!, $limit: Int!) {
  recentSubmissionList(username: $username, limit: $limit) {
    title
    timestamp
    statusDisplay
    lang
  }
}
"""

COOKIES = get_session_info()
username = input("Enter your leetcode username: ")

# GraphQL variables
variables = {"username": username, "limit": 10}

# Headers (some GraphQL requests need CSRF protection)
HEADERS = {
    "Content-Type": "application/json",
    "x-csrftoken": COOKIES["csrftoken"]
}

# Make the request
response = requests.post(URL, json={"query": GRAPHQL_QUERY, "variables": variables}, cookies=COOKIES, headers=HEADERS)

# Check response
if response.status_code == 200:
    data = response.json()
    print("\n✅ Recent Submissions:")
    for submission in data["data"]["recentSubmissionList"]:
        print(f"- {submission['title']} | {submission['statusDisplay']} | {submission['lang']} | Timestamp: {submission['timestamp']}")
else:
    print("\n❌ Failed to fetch data:", response.text)
