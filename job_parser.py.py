from pathlib import Path


def read_job_description(file_path):
    return Path(file_path).read_text(encoding="utf-8")


if __name__ == "__main__":
    job_path = Path("data") / "jobs" / "sample_job.txt"
    job_text = read_job_description(job_path)

    print("===== JOB DESCRIPTION TEXT =====")
    print(job_text)
