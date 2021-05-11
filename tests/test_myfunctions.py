from mylib import myfunctions

def test_lib_works():
    assert myfunctions.test('Ryan') == 'Hello Ryan'

def test_lib_error():
    assert myfunctions.test('Ryan') == 'Hello World'