from flow.backoffice.backoffice import BackofficeStage
from flow.client.stiner_stage import StinerStage


class StinerContainer:
    def __init__(self, driver):
        self.driver = driver

    @property
    def client(self) -> StinerStage:
        return StinerStage(self.driver)

    @property
    def backoffice(self) -> BackofficeStage:
        return BackofficeStage(self.driver)
