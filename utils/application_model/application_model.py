from test_library.src.application_model import ApplicationModel

from utils.application_model.top_menu.menu import TopMenuBase


class OverwrittenApplicationModel(ApplicationModel):

    @property
    def top_menu(self) -> TopMenuBase:
        return TopMenuBase(self.actions)
