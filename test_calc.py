import pytest
from pycode.cal import Calculator


class TestCalc:
	def setup_class(self):
		self.calc = Calculator()
		print("开始计算")

	def teardown_class(self):
		print("结束计算")

	@pytest.mark.parametrize("a,b,expected", [
		(3, 5, 8), (-1, -2, -3), (100, 200, 300)
	], ids=["int", "minus", "bigint"])
	def test_add(self, a, b, expected):
		assert expected == self.calc.add(a, b)

	@pytest.mark.parametrize("a,b,expected", [
		(2, 1, 1), (-2, -1, -1), (200, 90, 110)
	], ids=["int", "minus", "bigint"])
	def test_sub(self, a, b, expected):
		assert expected == self.calc.sub(a, b)


	@pytest.mark.parametrize("a,b,expected", [
		(2, 1, 2), (-2, -1, 2), (20, 90, 1800)
	], ids=["int", "minus", "bigint"])
	def test_mul(self, a, b, expected):
		assert expected == self.calc.mul(a, b)

	@pytest.mark.parametrize("a,b,expected", [
		(2, 1, 2), (-2, -1, 2), (0,1,0),
	], ids=["int", "minus", "0"])
	def test_div(self, a, b, expected):
		assert expected == self.calc.div(a, b)