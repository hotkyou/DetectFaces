from enum import Enum
from .functions import Functions as fc

class JP_kana(Enum):
    A, I, U, E, O = fc.jp_a(), fc.jp_i(), fc.jp_u(), fc.jp_e(), fc.jp_o()

class JP_line(Enum):
    A = [JP_kana.A, JP_kana.I, JP_kana.U, JP_kana.E, JP_kana.O]