def zero_shot_prompt(profile):
    return f"""
You are an expert AI career advisor.

Based on the following profile, suggest:
1. Suitable career role
2. required skills
3. A learning roadmap

Profiles:
{profile}
"""


def few_shot_prompt(profile):
    return f"""
You are an expert Ai career advisor.

Example:
Profile: B.Tech Mechanical, Python, Excel
Output:
Recommended Role: Data Analyst
Skills: SQL, Power BI
Roadmap: Learn SQL -> Build projects -> Apply

Example:
Profile: B.Tech Computer Science, Python, AI, Statistics
Output:
Recomemended Role: AI Engineer
Skills: Mathematics, Python, ML Algorithms
Roadmap: Learn Statistics, ML implementation, LLMs, Transformers, AI Agents

Now analyze this profile:
{profile}
"""
