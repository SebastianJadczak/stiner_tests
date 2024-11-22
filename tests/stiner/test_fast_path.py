from pathlib import PurePath
import pytest as pytest
from selenium.webdriver.chrome.options import Options

from src.pages.stiner.data import StinerData
from src.pages.stiner.explore.trails.data import TrailsPageData
from src.paths import Paths
from tests.stiner.common_path import CommonPath
from utils.env import CI_CD_env, CI_CD
from utils.utils import get_test_data_from_json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_path_to_test_data(test_data: str) -> PurePath:
    return Paths.test_data(test_data=test_data)


@pytest.fixture
def data_01_fast():
    return get_test_data_from_json(StinerData, get_path_to_test_data('data_01_fast'))


@pytest.fixture
def data_02_fast():
    return get_test_data_from_json(TrailsPageData, get_path_to_test_data('data_02_fast'))


class TestFastPath:

    @pytest.fixture(autouse=True)
    def setup(self):
        chrome_options = Options()
        if CI_CD_env is CI_CD.YES:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_01_fast(self, data_01_fast: StinerData):
        CommonPath(self.driver).test_fast_path(data=data_01_fast)
