import typing as t
from enum import Enum

from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.ships_locator import ShipsLocator


class Gun(object):
    class ShotResultEnum(Enum):
        MISS = 0
        SHIP_WOUNDED = 1
        SHIP_DESTROYED = 2
        ALREADY_SHOT = 3

    def __init__(
        self,
        battlefield: Battlefield,
        ships_locator: ShipsLocator,
        hited_cells: t.Set[Cell] = None,
    ):
        self._battlefield = battlefield
        self._ships_locator = ships_locator
        self._hited_cells: t.Set[Cell] = hited_cells or set()

    @property
    def hited_cells(self):
        return self._hited_cells

    def shot(self, cell: Cell) -> ShotResultEnum:
        if not self._battlefield.is_cell_internal(cell):
            raise Exception("cell outside battlefield")

        ship_location = self._ships_locator.get_ship_location_by_cell(cell)
        self._hited_cells.add(cell)
        if ship_location:
            ship_cell_index = ship_location.get_ship_cell_index(cell)
            hited = ship_location.ship.hit(ship_cell_index)

            if not hited:
                return self.ShotResultEnum.ALREADY_SHOT

            if ship_location.ship.is_destroyed():
                return self.ShotResultEnum.SHIP_DESTROYED
            return self.ShotResultEnum.SHIP_WOUNDED
        return self.ShotResultEnum.MISS
