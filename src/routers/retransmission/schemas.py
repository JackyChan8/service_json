from typing import Union, Any
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
    dldate: date
    plquan: int
    price: int
    sumavans: int
    sumlp: int
    sumvp: int
    sumdl: int
    suminv: float
    valos: float
    sumos: float
    fpay: int
    opay: int
    statdate: date
    admdate: date
    admavdldate: date
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
    exdate: date
    rep: str
    purp: str
    val: int
    addinc: int
    avans: int
    bonus: int
    agsum: int
    dua: str
    dup: str
    duz: str
    duc: str
    status: str

    @field_validator('dldate', 'statdate', 'admdate', 'admavdldate', 'exdate', mode='before')
    def parse_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, '%d-%m-%Y').date()  # Укажите нужный формат
        return value
