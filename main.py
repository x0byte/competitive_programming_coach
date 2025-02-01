from get_from_leetcode import fetch_submissions
from huggingface_hub import InferenceApi
import requests

def main():
    submissions_dict = fetch_submissions()

    prompt = f"""
    Act as a coding interview coach. Analyze the user's LeetCode submission history below to identify their weak areas and recommend specific practice questions to improve. Group results by problem type and error pattern.

    **Submission Data**:
    {submissions_dict}

    Focus on:
    1. Common error patterns (e.g., binary search edge cases, sliding window inefficiency).
    2. Recommended LeetCode questions to address gaps.
    3. Study strategies for each problem type.
    """


if __name__ == "__main__":
    main()