import allure
import pytest

class Test_001:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a",[1,2,3])
    def test_001(self, a):
        assert a!= 2
    @allure.step(title="测试步骤002")
    @pytest.mark.parametrize("c",[1,2,3])
    def test_002(self, c):
        assert a!= 2
