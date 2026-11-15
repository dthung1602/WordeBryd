import os
import requests
from tqdm.contrib.concurrent import thread_map

size = 256 * 1024
estimated = 10_000


# Generate ranges
ranges = [i * size for i in range(estimated)]

def task(start):
    end = start + size
    chunk_name = f"{start}-{end}"
    file_name = f"public/resources/windows2000/windows-{chunk_name}.img"

    # Fast skip check
    if os.path.exists(file_name):
        return "skipped"

    try:
        res = requests.get(f"https://c.copy.sh/windows2k-v2/{chunk_name}.img", timeout=10)

        if res.status_code == 404:
            # Tell thread_map to stop by raising an exception, or return a signal
            raise StopIteration(f"End of file reached at offset {start}")

        res.raise_for_status()

        with open(file_name, "wb") as f:
            f.write(res.content)
        return "downloaded"

    except requests.RequestException as e:
        # Gracefully handle network hiccups without breaking tqdm
        return f"error: {e}"

# thread_map safely binds ThreadPoolExecutor + tqdm + as_completed
# while managing underlying worker thread throttling.
try:
    results = thread_map(task, ranges, max_workers=8, desc="Downloading")
except StopIteration as e:
    # Safely break out of execution when the 404 EOF is tripped
    print(f"\n[!] Finished: {e}")
