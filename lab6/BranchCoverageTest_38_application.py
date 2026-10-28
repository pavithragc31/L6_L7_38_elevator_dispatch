
from elevator_dispatch import next_direction, door_action, pick_elevator


# Branch coverage tests for next_direction()
def test_up_with_request_above():
    assert next_direction(3, "up", [5]) == "up"


def test_up_with_only_request_below():
    assert next_direction(5, "up", [2]) == "down"


def test_up_with_no_requests():
    assert next_direction(3, "up", []) == "idle"


def test_down_with_request_below():
    assert next_direction(5, "down", [2]) == "down"


def test_down_with_only_request_above():
    assert next_direction(3, "down", [7]) == "up"


def test_down_with_no_requests():
    assert next_direction(3, "down", []) == "idle"


def test_other_direction_with_request_above():
    assert next_direction(3, "idle", [5]) == "up"


def test_other_direction_with_request_below():
    assert next_direction(5, "idle", [2]) == "down"


def test_other_direction_with_no_requests():
    assert next_direction(3, "idle", []) == "idle"


# Branch coverage tests for door_action()
def test_emergency_branch():
    assert door_action(700, True, True) == "hold_open"


def test_overload_branch():
    assert door_action(631, False, False) == "overload"


def test_blocked_branch():
    assert door_action(500, True, False) == "reopen"


def test_normal_close_branch():
    assert door_action(500, False, False) == "close"


def test_load_exactly_at_limit():
    assert door_action(630, False, False) == "close"


# Branch coverage tests for pick_elevator()
def test_empty_car_list():
    assert pick_elevator([], 3) is None


def test_first_car_selected():
    assert pick_elevator([("A", 2, True)], 3) == "A"


def test_second_car_has_smaller_gap():
    cars = [("A", 1, True), ("B", 3, True)]
    assert pick_elevator(cars, 3) == "B"


def test_second_car_has_larger_gap():
    cars = [("A", 3, True), ("B", 8, True)]
    assert pick_elevator(cars, 3) == "A"


def test_busy_car_penalty():
    cars = [("A", 3, False), ("B", 5, True)]
    assert pick_elevator(cars, 3) == "B"
