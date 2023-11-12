import subprocess


def checkout(cmd: str, text: str) -> bool:
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0 and (text in result.stdout or text in result.stderr):
        return True

    return False


