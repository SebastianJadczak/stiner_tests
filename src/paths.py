from pathlib import Path


class Paths:
    ROOT = Path(__file__).parent.parent
    TESTS_DIR = ROOT / 'tests'
    TEST_DATA_DIR = TESTS_DIR / 'data'

    @classmethod
    def test_data(cls, test_data: str) -> Path:
        return cls.TEST_DATA_DIR / f'{test_data}.json'
