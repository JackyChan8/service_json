from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, Text, CHAR, DATE, func

from src.models.base_class import Base


class PortfolioV01(Base):
    """
        PortfolioV01 Table
    """
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    num: Mapped[int] = mapped_column(Integer)
    dl: Mapped[str] = mapped_column(Text)
    pl: Mapped[str] = mapped_column(Text)
    kontragent: Mapped[str] = mapped_column(Text)
    dltype: Mapped[str] = mapped_column(CHAR(1))
    dlnum: Mapped[str] = mapped_column(Text)
    dldate: Mapped[str] = mapped_column(DATE, nullable=True)
    plquan: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(Integer)
    sumavans: Mapped[int] = mapped_column(Integer)
    sumlp: Mapped[int] = mapped_column(Integer)
    sumvp: Mapped[int] = mapped_column(Integer)
    sumdl: Mapped[int] = mapped_column(Integer)
    suminv: Mapped[int] = mapped_column(Integer)
    valos: Mapped[int] = mapped_column(Integer)
    sumos: Mapped[int] = mapped_column(Integer)
    fpay: Mapped[int] = mapped_column(Integer)
    opay: Mapped[int] = mapped_column(Integer)
    statdate: Mapped[str] = mapped_column(DATE, nullable=True)
    admdate: Mapped[str] = mapped_column(DATE, nullable=True)
    admavdldate: Mapped[str] = mapped_column(DATE, nullable=True)
    supp: Mapped[str] = mapped_column(Text)
    catavto: Mapped[str] = mapped_column(CHAR(1))
    comtr: Mapped[str] = mapped_column(CHAR(3))
    div: Mapped[str] = mapped_column(Text)
    men: Mapped[str] = mapped_column(Text)
    brand: Mapped[str] = mapped_column(Text)
    mod: Mapped[str] = mapped_column(Text)
    mar: Mapped[int] = mapped_column(Integer)
    bid: Mapped[int] = mapped_column(Integer)
    lp: Mapped[str] = mapped_column(Text)
    term: Mapped[int] = mapped_column(Integer)
    aff: Mapped[str] = mapped_column(Text)
    ist: Mapped[str] = mapped_column(Text)
    secl: Mapped[str] = mapped_column(CHAR(3))
    addtype: Mapped[str] = mapped_column(Text)
    exdate: Mapped[str] = mapped_column(DATE, nullable=True)
    rep: Mapped[str] = mapped_column(CHAR(3))
    purp: Mapped[str] = mapped_column(Text)
    val: Mapped[int] = mapped_column(Integer)
    addinc: Mapped[int] = mapped_column(Integer)
    avans: Mapped[int] = mapped_column(Integer)
    bonus: Mapped[int] = mapped_column(Integer)
    agsum: Mapped[int] = mapped_column(Integer)
    dua: Mapped[str] = mapped_column(Text)
    dup: Mapped[str] = mapped_column(Text)
    duz: Mapped[str] = mapped_column(Text)
    duc: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(Text)
    insert_date: Mapped[datetime] = mapped_column(DATE, default=func.now())
    insert_file: Mapped[str] = mapped_column(Text, nullable=True)
