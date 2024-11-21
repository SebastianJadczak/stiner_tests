from dataclasses import dataclass

from src.pages.stiner.create_your_trail.tabs.add_information.data import AddInformationTabData
from src.pages.stiner.create_your_trail.tabs.choose_attractions.data import ChooseAttractionsTabData


@dataclass
class CreateYourTrailPageData:
    choose_attractions_tab: ChooseAttractionsTabData
    add_information_tab: AddInformationTabData

