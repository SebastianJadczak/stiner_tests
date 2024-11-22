from dataclasses import dataclass

from src.pages.stiner.favorite.tabs.all.data import AllTabData
from src.pages.stiner.favorite.tabs.points.data import PointsTabData
from src.pages.stiner.favorite.tabs.trails.data import TrailsTabData


@dataclass
class FavoritePageData:
    all_tab: AllTabData
    points_tab: PointsTabData
    trails_tab: TrailsTabData
