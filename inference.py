import os
from openai import OpenAI
from env.environment import HealthcareEnv
from env.tasks import TASKS
from env.grader import grade


client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

def get_action_from_llm(symptoms):
    prompt = f"""
    Patient symptoms: {symptoms}.
    Choose the most likely disease from:
    flu, heart_disease, migraine.

    Only return ONE word.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


def run():
    print("[START]")

    env = HealthcareEnv()

    for task in TASKS:
        print(f"[TASK] {task['name']}")

        state = env.reset()
        done = False
        steps = 0

        while not done and steps < 5:
            symptoms = state["symptoms"]


            action = get_action_from_llm(symptoms)

            new_state, reward, done, _ = env.step(action)

            print(f"[STEP] action={action} reward={reward}")

            state = new_state
            steps += 1

        score = grade(task["name"], state)
        print(f"[RESULT] task={task['name']} score={score}")

    print("[END]")


if __name__ == "__main__":
    run()