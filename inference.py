from env.environment import HealthcareEnv
from env.tasks import TASKS
from env.grader import grade

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

            if "fever" in symptoms:
                action = "flu"
            elif "chest_pain" in symptoms:
                action = "heart_disease"
            else:
                action = "migraine"

            new_state, reward, done, _ = env.step(action)

            print(f"[STEP] action={action} reward={reward}")

            state = new_state
            steps += 1

        score = grade(task["name"], state)

        print(f"[RESULT] task={task['name']} score={score}")

    print("[END]")


if __name__ == "__main__":
    run()