# LeetCoach 🤖 – Your Personal Competitive Coding Coach (Because We All Suck Sometimes) 🎯

Welcome to LeetCoach, the project that tells you why you keep failing at LeetCode (but nicely, I promise)!

This was inspired by my own suffering, where I kept getting "Wrong Answer" and "Time Limit Exceeded" until I finally snapped and thought:
_"What if a bot could tell me what I’m doing wrong and help me improve?"_

So here we are! 🎉

### 📌 What Does This Magical Coach Do?

* 🚀 Pulls your submission data from LeetCode’s GraphQL API (Yes, LeetCode has GraphQL. Mind-blowing, I know).
* 🔍 Analyzes your failed submissions and tells you what’s wrong (whether you want to hear it or not).
* 📈 Figures out patterns in your mistakes (like why your binary search always crashes).
* 💡 Gives personalized practice problems to fix your weak spots (so you stop brute-forcing DP problems like a caveman).
* 😂 Does NOT judge you (too much).


### 🛠️ How It Works

* You log into LeetCode, and we grab your submission data using GraphQL API.
  * We analyze your misery:
      * Wrong Answer? Probably forgot an edge case.
      * TLE? Maybe don’t use O(N²) for large inputs.
      * MLE? No, you don’t need that many recursive calls.
* We recommend practice problems that actually help you get better at your weak topics.
* You get better (or at least, slightly less frustrated).

*Get your LeetCode session cookies (Because CAPTCHA exists 🤡):*

Log into LeetCode -> Open Developer Tools -> Application -> Cookies.

Copy LEETCODE_SESSION and csrftoken and save them in cookies.json:

    {
      "LEETCODE_SESSION": "your-session-token-here",
      "csrftoken": "your-csrf-token-here"
    }

Run the magic:

    python main.py

### 📌 Features (Fancy Stuff This Actually Does)

* ✅ Fetches your LeetCode submissions dynamically (no hardcoding, duh).
* ✅ Groups your submissions by errors (Wrong Answer, TLE, MLE, etc.).
* ✅ Analyzes patterns in your mistakes (so you stop making the same dumb error 10 times).
* ✅ Uses AI-generated insights (future feature 🤖).
* ✅ Recommends similar problems to strengthen your weak topics.
* ✅ Makes you less bad at coding interviews (hopefully).

### 📌 Example Output (Your Daily Roast)

📊 Common Mistakes:
- Koko Eating Bananas ❌ Wrong Answer (x2) → Maybe read the problem properly?
- Maximum Average Subarray I ⏳ Time Limit Exceeded → Ever heard of sliding window?
- Find Minimum in Rotated Sorted Array ❌ Wrong Answer → Binary search isn't magic, you know.

🏆 Suggested Practice Problems:
- Binary Search Fix: "Find Peak Element"
- Sliding Window Improvement: "Subarray Sum Equals K"
- DP Fix: "House Robber"

### 📌 Why Did I Make This?

Because I suck at LeetCode, and I wanted a bot to tell me where I’m going wrong without crushing my self-esteem too much.

If you also rage quit LeetCode after the 5th Wrong Answer, this is for you. 🚀

### 📌 Future Plans (Or Wishful Thinking)

* 🧠 AI-powered explanations ("Why you failed, in human language")
* 📊 Performance tracking (watch your suffering decrease over time)
* 🔥 Daily challenges (personalized problem sets)
* 📡 Web Dashboard (because CLI tools are for nerds)
