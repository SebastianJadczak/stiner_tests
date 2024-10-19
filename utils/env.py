import os
from enum import StrEnum


class CI_CD(StrEnum):
    NO = 'NO'
    YES = 'YES'


CI_CD_env = os.environ.get('CI_CD', CI_CD.NO)
