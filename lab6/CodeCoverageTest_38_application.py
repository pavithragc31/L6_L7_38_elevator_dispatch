
import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator


# Tests for next_direction()
def test_direction_up_with_requests_above():
    assert next_direction(3, "up", [5, 7]) == "up"


def test_direction_up_with_only_requests_below():
    assert next_direction(5, "up", [2]) == "down"


def test_direction_up_with_no_requests():
    assert next_direction(3, "up", []) == "idle"


def test_direction_down_with_requests_below():
    assert next_direction(5, "down", [2]) == "down"


def test_direction_down_with_only_requests_above():
    assert next_direction(3, "down", [5]) == "up"


def test_direction_down_with_no_requests():
    assert next_direction(3, "down", []) == "idle"


def test_other_direction_with_requests_above():
    assert next_direction(3, "idle", [5]) == "up"


def test_other_direction_with_requests_below():
    assert next_direction(5, "idle", [2]) == "down"


def test_other_direction_with_no_requests():
    assert next_direction(3, "idle", []) == "idle"


# Tests for door_action()
def test_emergency_holds_doors():
    assert door_action(100, False, True) == "hold_open"


def test_overload_opens_doors():
    assert door_action(631, False, False) == "overload"


def test_blocked_door_reopens():
    assert door_action(500, True, False) == "reopen"


def test_normal_door_closes():
    assert door_action(500, False, False) == "close"


def test_load_at_limit_is_not_overload():
    assert door_action(630, False, False) == "close"


# Tests for pick_elevator()
def test_pick_nearest_idle_elevator():
    cars = [("A", 2, True), ("B", 8, True)]
    assert pick_elevator(cars, 3) == "A"


def test_busy_elevator_gets_penalty():
    cars = [("A", 5, False), ("B", 8, True)]
    assert pick_elevator(cars, 5) == "B"


def test_first_elevator_wins_equal_gap():
    cars = [("A", 2, True), ("B", 4, True)]
    assert pick_elevator(cars, 3) == "A"


def test_empty_elevator_list():
    assert pick_elevator([], 3) is None


def test_busy_elevator_can_still_be_selected():
    cars = [("A", 1, False)]
    assert pick_elevator(cars, 1) == "A"
