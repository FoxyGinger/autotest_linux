import subprocess


def execute_func(cmd: str, expected_str: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0 and expected_str in result.stdout:
        return True

    return False
