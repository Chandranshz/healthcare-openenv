import os
from openai import OpenAI

from env.environment import HealthcareEnv
from env.tasks import TASKS
from env.grader import grade


def ask_llm(symptoms):
    client = OpenAI(
        api_key=os.environ["API_KEY"],
        base_url=os.environ["API_BASE_URL"]
    )

    prompt = f"""
    Patient symptoms: {symptoms}

    Choose the most likely disease from:
    flu, heart_disease, migraine

    Return only one word.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content.strip().lower()
    return answer


def run():
    env = HealthcareEnv()
    results = []

    for task in TASKS:
        state = env.reset()
        done = False
        steps = 0

        while not done and steps < 5:
            symptoms = state["symptoms"]

            try:
                action = ask_llm(symptoms)
            except Exception:
                action = "flu"

            if action not in ["flu", "heart_disease", "migraine"]:
                action = "flu"

            state, reward, done, _ = env.step(action)
            steps += 1

        score = grade(task["name"], state)

        results.append({
            "task": task["name"],
            "score": score
        })

    return {"results": results}


if __name__ == "__main__":
    print(run())