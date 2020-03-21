rem #python -m unittest test_module1 test_module2 

rem #同时测试多个module
rem #python -m unittest test_module.TestClass
rem #python -m unittest test_module.TestClass.test_method

rem #python -m unittest -v test_module
rem python -m unittest -v tests/unittest1_tests.py
rem python -m unittest -h
rem python -m unittest tests/unittest1_tests.py

rem cd tests
python -m unittest test_mathfunc.TestMathFunc