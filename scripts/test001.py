import allure
import pytest

class Test_001:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a",[1,5,3])
    def test_001(self, a):
        assert a!= 2
    @allure.step(title="测试步骤002")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("c", [1, 4, 3])
    def test_002(self, c):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert c!= 2
