def diagnosis_first(trajectory):
    """Check that assistant's first message is diagnostic."""
    first = next((t for t in trajectory if t["role"] == "assistant"), None)
    if first and "?" in first["content"]:
        return True
    return False

def single_question_per_step(trajectory):
    """Check that each assistant message asks <=1 learner task."""
    for t in trajectory:
        if t["role"] == "assistant":
            if t["content"].count("?") > 1:
                return False
    return True

def no_direct_answer_initially(trajectory):
    """Assistant shouldn't solve task immediately."""
    first_q = next((t for t in trajectory if t["role"] == "assistant"), None)
    if first_q and "print(" in first_q["content"]:
        return False
    return True
