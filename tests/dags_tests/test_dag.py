import package_a.my_dag as my_dag
import package_a.scripts.my_script as my_script
import package_b.my_mod as my_mod

def test_my_dag():
    assert my_dag.func() == "Hello World"

def test_my_script():
    assert my_script.trans() == "Hello trans"

def test_my_mod():
    assert my_mod.mod_fun() == "Hello mod"