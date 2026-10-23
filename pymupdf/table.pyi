from collections.abc import Iterator

class CellGroup:
    def __init__(self, cells) -> None: ...
    @property
    def cells(self) -> list[tuple[float, float, float, float]]: ...

class TableRow(CellGroup): ...

class TableHeader:
    bbox: tuple[float, float, float, float]
    cells: list[tuple[float, float, float, float]]
    names: list[str]
    external: bool
    def __init__(
        self,
        bbox: tuple[float, float, float, float],
        cells: list[tuple[float, float, float, float]],
        names: list[str],
        above: bool,
    ) -> None: ...

class SpanCell:
    bbox: tuple[float, float, float, float] | None
    text: str
    colspan: int
    rowspan: int
    tag: str
    def __init__(
        self,
        bbox: tuple[float, float, float, float] | None,
        text: str,
        colspan: int,
        rowspan: int,
        tag: str = "td",
    ) -> None: ...

class Table:
    @property
    def page(self): ...
    @property
    def textpage(self): ...
    @property
    def bbox(self) -> tuple[float, float, float, float]: ...
    def extract(self) -> list[list[str | None]]: ...
    @property
    def rows(self) -> list[TableRow]: ...
    @property
    def header(self) -> TableHeader: ...
    @header.setter
    def header(self, value: TableHeader) -> None: ...
    @property
    def cells(self) -> list[tuple[float, float, float, float]]: ...
    placements: list[list[SpanCell]] | None
    header_rows: int
    section_rows: tuple[int, ...]
    def to_html(self) -> str: ...

class TableFinder:
    @property
    def tables(self) -> list[Table]: ...
    def __iter__(self) -> Iterator[Table]: ...
