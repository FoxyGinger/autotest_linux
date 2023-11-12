from command_func import checkout


tst = "/home/user/tst"
out = "/home/user/out"
folder1 = "/home/user/folder1"


def test_step1():
    # test1
    result1 = checkout(f"cd {tst}; 7z a {out}/arx2", "Everything is Ok")
    result2 = checkout(f"cd {out}; ls", "arx2.7z")

    assert result1 and result2, "test1 FAIL"


def test_step2():
    # test2
    result1 = checkout(f"cd {out}; 7z e arx2.7z -o {folder1} -y", "Everything is Ok")
    result2 = checkout(f"cd {folder1}; ls", "qwe")
    result3 = checkout(f"cd {folder1}; ls", "rty")

    assert result1 and result2 and result3, "test2 FAIL"


def test_step3():
    # test3
    assert checkout(f"cd {out}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout(f"cd {tst}; 7z u ../out/arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5
    assert checkout(f"cd {out}; 7z d arx2.7z", "Everything is Ok"), "test5 FAIL"
