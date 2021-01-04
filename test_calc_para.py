import pytest
import yaml
import allure

from pycode.cal import Calculator


def get_datas():
	with open("./data.yml") as f:
		datas = yaml.safe_load(f)
		print(datas)
		add_datas = datas["datas_add"]
		add_ids = datas["myid"]
		sub_datas = datas["datas_sub"]
		mul_datas = datas["datas_mul"]
		div_datas = datas["datas_div"]
		return [add_datas, add_ids,sub_datas,mul_datas,div_datas]

class TestCalc:
	'''	def setup_class(self):
			self.calc = Calculator()
			print("开始计算")

		def teardown_class(self):
			print("结束计算")
	'''
	'''
	@pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("./data.yml"))["datas"]
											, ids=yaml.safe_load(open("./data.yml"))["myid"])
	'''
	@pytest.mark.run(order=2)
	@pytest.mark.parametrize("a,b,expected",get_datas()[0],ids=get_datas()[1])
	def test_add(self, a, b, expected, myfixture):
		assert expected == myfixture.add(a, b)

	@pytest.mark.run(order=1)
	@pytest.mark.parametrize("a,b,expected", get_datas()[2], ids=get_datas()[1])
	def test_sub(self, a, b, expected,myfixture):
		assert expected == myfixture.sub(a, b)

	@pytest.mark.run(order=3)
	@pytest.mark.parametrize("a,b,expected", get_datas()[3],ids=get_datas()[1])
	def test_mul(self, a, b, expected,myfixture):
		assert expected == myfixture.mul(a, b)

	@pytest.mark.run(order=4)
	@allure.step("除法")
	@pytest.mark.parametrize("a,b,expected", get_datas()[4],ids=get_datas()[1])
	def test_div(self, a, b, expected,myfixture):
		assert expected == myfixture.div(a, b)

