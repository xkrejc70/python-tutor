import subprocess

# Run code analysis using pylint
def run_code_analysis(file_path):
    result = subprocess.run(['pylint', '--msg-template="line {line}: [{msg_id}-{symbol}] {msg}"', '--disable=C0301', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return {
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    }