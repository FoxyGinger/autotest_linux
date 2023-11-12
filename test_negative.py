from command_func import checkout


def test_step1():
    # test1
    assert checkout("cd /home/user/out; 7z e bad_arx.7z -o /home/user/folder1 -y", "ERRORS"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout("cd /home/user/tst; 7z t bad_arx.7z", "ERRORS"), "test2 FAIL"

