import subprocess
import sys

def test_random_joke():
    process = subprocess.Popen(
        [sys.executable, "examples/random_joke.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()

    assert process.returncode == 0, f"Script failed with error: {stderr.decode()}"
    assert stdout, "Script did not produce any output."
