def grade(task_name, final_state):
    if final_state.get("diagnosis_correct"):
        return 1.0
    return 0.0