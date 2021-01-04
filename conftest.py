import pytest
from pycode.cal import Calculator

def get_db_data():
	return ['参数1','参数2']


@pytest.fixture(scope="module")
def myfixture():
	calc=Calculator()
	print("开始计算")
	yield calc
	print("结束计算")

'''
@pytest.fixture(params=['参数1','参数2'])     #autouse=True 每一个case都会执行
def myfixture2(request):
	print("不同的fixture,里面的参数是{}".format(request.param))
	env = request.param
	return env
'''
'''
@pytest.fixture(params=get_db_data())     #autouse=True 每一个case都会执行
def myfixture2(request):
	print("不同的fixture,里面的参数是{}".format(request.param))
	env = request.param
	return env
'''