from typing import Union, Any, Optional
from datetime import datetime, date

from pydantic import BaseModel, RootModel, field_validator


class AnyJson(RootModel):
    root: Union[dict[str, Any], list[dict[str, Any]]]


class PortfolioSchema(BaseModel):
    """
        Portfolio Schema
    """
    num: int
    dl: str
    pl: str
    kontragent: str
    dltype: str
    dlnum: str
    dldate: Optional[date] = None
    plquan: int
    price: float
    sumavans: float
    sumlp: float
    sumvp: float
    sumdl: float
    suminv: float
    valos: float
    sumos: float
    fpay: float
    opay: float
    statdate: Optional[date] = None
    admdate: Optional[date] = None
    admavdldate: Optional[date] = None
    supp: str
    catavto: str
    comtr: str
    div: str
    men: str
    brand: str
    mod: str
    mar: float
    bid: int | float
    lp: str
    term: int
    aff: str
    ist: str
    secl: str
    addtype: str
    exdate: Optional[date] = None
    rep: str
    purp: str
    val: float
    addinc: int
    avans: float
    bonus: float
    agsum: int
    dua: str
    dup: str
    duz: str
    duc: str
    status: str

    @field_validator('dldate', 'statdate', 'admdate', 'admavdldate', 'exdate', mode='before')
    def parse_date(cls, value):
        if isinstance(value, str):
            if len(value) > 0:
                return datetime.strptime(value, '%d-%m-%Y').date()  # Укажите нужный формат
            else:
                return None
        return value
