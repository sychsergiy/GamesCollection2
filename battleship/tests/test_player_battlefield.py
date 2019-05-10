from battleship.player_battlefield import PlayerBattlefield
from battleship.player import Player
from battleship.battlefield import Battlefield
from battleship.game_mode import GameMode


def test_player_battlefield_not_ready_to_start():
    ship_size_count_map = {1: 4, 2: 2}
    game_mode = GameMode(Battlefield(4, 4), ship_size_count_map)

    p_b = PlayerBattlefield(Player("player"), game_mode)
    assert p_b.locate_ship(0, 0, ship_size=1) == True
    assert p_b.locate_ship(0, 0, ship_size=1) == False
    assert p_b._ships_counter._ship_size_count_map[1] == 3

    assert p_b.ready_to_start == False
    assert p_b.set_ready_to_start() == False
    assert p_b.ready_to_start == False


def test_player_battlefield_ready_to_start():
    ship_size_count_map = {1: 2}
    game_mode = GameMode(Battlefield(4, 4), ship_size_count_map)

    p_b = PlayerBattlefield(Player("player"), game_mode)
    assert p_b.locate_ship(0, 0, ship_size=1) == True
    assert p_b.locate_ship(3, 3, ship_size=1) == True
    assert p_b.locate_ship(0, 1, ship_size=1) == False
    assert p_b._ships_counter._ship_size_count_map[1] == 0

    assert p_b.ready_to_start == False
    assert p_b.set_ready_to_start() == True
    assert p_b.ready_to_start == True
