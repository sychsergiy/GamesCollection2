from games_collection.games.battleship.battlefield import Battlefield
from games_collection.games.battleship.cell import Cell
from games_collection.games.battleship.gun import Gun
from games_collection.games.battleship.ship import Ship
from games_collection.games.battleship.ship_location import (
    HorizontalShipLocation,
)
from games_collection.games.battleship.ship_locator import ShipLocator
from games_collection.games.battleship.ships_locator import ShipsLocator


def test_horizontal_ship_location():
    battlefield = Battlefield(5, 5)
    ships_locator = ShipsLocator(battlefield)
    locator = ShipLocator(battlefield, ships_locator)
    ship = Ship(2)
    ship_location = HorizontalShipLocation(ship, Cell(2, 2))
    first_ship_located = locator.locate_ship(ship_location)
    assert first_ship_located

    shot_manager = Gun(battlefield, ships_locator)
    first_shot_result = shot_manager.shot(Cell(2, 2))
    assert first_shot_result == Gun.ShotResultEnum.SHIP_WOUNDED
    second_shot_result = shot_manager.shot(Cell(3, 2))
    assert second_shot_result == Gun.ShotResultEnum.SHIP_DESTROYED
    third_shot_result = shot_manager.shot(Cell(2, 2))
    assert third_shot_result == Gun.ShotResultEnum.ALREADY_SHOT
    fourth_shot_result = shot_manager.shot(Cell(1, 1))
    assert fourth_shot_result == Gun.ShotResultEnum.MISS
