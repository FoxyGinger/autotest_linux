import subprocess


def execute_func(cmd: str, expected_str: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    out = result.stdout.decode(encoding='utf-8')
    if expected_str in out:
        return True

    return False
