from get_from_leetcode import fetch_submissions
from huggingface_hub import login
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM


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

    api_key = input("Enter your huggingface API key: ")

    # Authenticate (ensures access to API)
    login(token=api_key)

    model_name = "mistralai/Mistral-Small-24B-Instruct-2501"

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

    # Load model with remote code execution
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

    # Load pipeline
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    # Run inference
    output = generator(prompt, max_new_tokens=100, truncation=True)
    print("📝 Generated Text:", output[0]["generated_text"])




if __name__ == "__main__":
    main()