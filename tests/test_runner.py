import os
import subprocess

def run_tests():
    # List of server directories
    servers = ["server/flask", "server/test", "server/model"]

    # Loop through each server directory and run tests
    for server in servers:
        tests_path = os.path.join(server, "tests")
        if os.path.exists(tests_path):
            os.chdir(server)
            subprocess.run(["pytest", "tests"])
            os.chdir("..")

if __name__ == "__main__":
    run_tests()
