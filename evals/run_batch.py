# evals/run_batch.py
import os
import asyncio
import json
from glob import glob
from pathlib import Path

# import the runner from the file you already added
# adjust import path if needed, e.g. from evals.session_runner import run_study_session_trajectory
from session_runner import run_study_session_trajectory  # <- ensure PYTHONPATH includes evals/

SEEDS_DIR = Path(__file__).resolve().parents[1] / "seeds"   # repo/seeds
ARTIFACTS_DIR = Path(__file__).resolve().parents[1] / "artifacts"
ARTIFACTS_DIR.mkdir(exist_ok=True)

async def process_file(filepath: str, *, mock_mode: bool = True):
    with open(filepath, "r", encoding="utf-8") as f:
        session_json = json.load(f)

    # run the session trajectory (mock_mode True for offline)
    artifact = await run_study_session_trajectory(session_json, mock_mode=mock_mode)

    # write per-session artifact
    session_id = artifact.get("session_id") or Path(filepath).stem
    out_path = ARTIFACTS_DIR / f"{session_id}.artifact.json"
    with open(out_path, "w", encoding="utf-8") as wf:
        json.dump(artifact, wf, indent=2)

    # also append to a master jsonl
    jsonl_path = ARTIFACTS_DIR / "artifacts.jsonl"
    with open(jsonl_path, "a", encoding="utf-8") as jf:
        jf.write(json.dumps(artifact) + "\n")

    print(f"Processed {filepath} -> {out_path}")
    return out_path

async def run_all(mock_mode: bool = True):
    files = sorted(glob(str(SEEDS_DIR / "*.json")))
    print(f"Found {len(files)} seed files in {SEEDS_DIR}")
    results = []
    for fp in files:
        res = await process_file(fp, mock_mode=mock_mode)
        results.append(str(res))
    print("Done. Artifacts written to", ARTIFACTS_DIR)
    return results

if __name__ == "__main__":
    # change mock_mode=False when wiring a real AsyncOpenAI client (and pass client into run_study_session_trajectory)
    asyncio.run(run_all(mock_mode=True))
