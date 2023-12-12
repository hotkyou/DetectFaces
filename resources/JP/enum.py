from enum import Enum
from .functions import Functions as fc

class JP_kana(Enum):
    A, I, U, E, O = fc.jp_a(), fc.jp_i(), fc.jp_u(), fc.jp_e(), fc.jp_o()
    KA, KI, KU, KE, KO = fc.jp_ka(), fc.jp_ki(), fc.jp_ku(), fc.jp_ke(), fc.jp_ko()
    SA, SHI, SU, SE, SO = fc.jp_sa(), fc.jp_shi(), fc.jp_su(), fc.jp_se(), fc.jp_so()
    TA, CHI, TSU, TE, TO = fc.jp_ta(), fc.jp_chi(), fc.jp_tsu(), fc.jp_te(), fc.jp_to()
    NA, NI, NU, NE, NO = fc.jp_na(), fc.jp_ni(), fc.jp_nu(), fc.jp_ne(), fc.jp_no()
    HA, HI, FU, HE, HO = fc.jp_ha(), fc.jp_hi(), fc.jp_fu(), fc.jp_he(), fc.jp_ho()
    MA, MI, MU, ME, MO = fc.jp_ma(), fc.jp_mi(), fc.jp_mu(),fc.jp_me(), fc.jp_mo()
    YA, YU, YO = fc.jp_ya(), fc.jp_yu(), fc.jp_yo()
    RA, RI, RU, RE, RO = fc.jp_ra(), fc.jp_ri(), fc.jp_ru(), fc.jp_re(), fc.jp_ro()
    WA, WO, N = fc.jp_wa(), fc.jp_wo(), fc.jp_n()

class JP_line(Enum):
    A = [JP_kana.A, JP_kana.I, JP_kana.U, JP_kana.E, JP_kana.O]
    KA = [JP_kana.KA, JP_kana.KI, JP_kana.KU, JP_kana.KE, JP_kana.KO]
    SA = [JP_kana.SA, JP_kana.SHI, JP_kana.SU, JP_kana.SE, JP_kana.SO]
    TA = [JP_kana.TA, JP_kana.CHI, JP_kana.TSU, JP_kana.TE, JP_kana.TO]
    NA = [JP_kana.NA, JP_kana.NI, JP_kana.NU, JP_kana.NE, JP_kana.NO]
    HA = [JP_kana.HA, JP_kana.HI, JP_kana.FU, JP_kana.HE, JP_kana.HO]
    MA = [JP_kana.MA, JP_kana.MI, JP_kana.MU, JP_kana.ME, JP_kana.MO]
    YA = [JP_kana.YA, JP_kana.YU, JP_kana.YO]
    RA = [JP_kana.RA, JP_kana.RI, JP_kana.RU, JP_kana.RE, JP_kana.RO]
    WA = [JP_kana.WA, JP_kana.WO, JP_kana.N]
    
class JP_kana_list(Enum):
    A = [JP_kana.A, JP_kana.KA, JP_kana.SA, JP_kana.TA, JP_kana.NA, JP_kana.HA, JP_kana.MA, JP_kana.YA, JP_kana.RA, JP_kana.WA]
    I = [JP_kana.I, JP_kana.KI, JP_kana.SHI, JP_kana.CHI, JP_kana.NI, JP_kana.HI, JP_kana.MI, JP_kana.YU, JP_kana.RI]
    U = [JP_kana.U, JP_kana.KU, JP_kana.SU, JP_kana.TSU, JP_kana.NU, JP_kana.FU, JP_kana.MU, JP_kana.YU, JP_kana.RU]
    E = [JP_kana.E, JP_kana.KE, JP_kana.SE, JP_kana.TE, JP_kana.NE, JP_kana.HE, JP_kana.ME, JP_kana.RE]
    O = [JP_kana.O, JP_kana.KO, JP_kana.SO, JP_kana.TO, JP_kana.NO, JP_kana.HO, JP_kana.MO, JP_kana.YO, JP_kana.RO, JP_kana.WO, JP_kana.N]