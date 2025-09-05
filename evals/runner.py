import json, glob
from heuristics import diagnosis_first, single_question_per_step, no_direct_answer_initially

def run_eval(seed_path):
    with open(seed_path) as f:
        session = json.load(f)
    traj = session["trajectory"]

    results = {
        "diagnosis_first": diagnosis_first(traj),
        "single_question": single_question_per_step(traj),
        "no_direct_answer_initially": no_direct_answer_initially(traj)
    }
    return results

if __name__ == "__main__":
    for file in glob.glob("seeds/*.json"):
        print(file, run_eval(file))
