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

def fetch_submissions():

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
    variables = {"username": username, "limit": 20}

    # Headers
    HEADERS = {
        "Content-Type": "application/json",
        "x-csrftoken": COOKIES["csrftoken"]
    }

    # Make the request
    response = requests.post(URL, json={"query": GRAPHQL_QUERY, "variables": variables}, cookies=COOKIES, headers=HEADERS)

    # Check response
    if response.status_code == 200:
        data = response.json()
        submissions_dict = {}
        for submission in data["data"]["recentSubmissionList"]:
            key = submission['statusDisplay']
            if key not in submissions_dict:
                submissions_dict[key] = []
            submissions_dict[key].append({
                "title": submission['title'],
                "lang": submission['lang']
            })
    else:
        print("\n❌ Failed to fetch data:", response.text)

    return submissions_dict
