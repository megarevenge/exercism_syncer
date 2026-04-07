"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagon_id, missing_wagons):
    """
    Moves first two wagons to the end and inserts missing_wagons 
    directly after the locomotive (ID 1).
    """
    # 1. Separate the first two wagons and the rest of the train
    misplaced_wagons = each_wagon_id[:2]
    remaining_train = each_wagon_id[2:]
    
    # 2. Locate the locomotive (ID 1) in the remaining train
    locomotive_index = remaining_train.index(1)
    
    # 3. Slice the train into 'before locomotive', 'locomotive', and 'after locomotive'
    # Since we need to insert AFTER the locomotive, we take up to the locomotive index + 1
    head = remaining_train[:locomotive_index + 1]
    tail = remaining_train[locomotive_index + 1:]
    
    # 4. Reconstruct the train in the correct order
    # Locomotive-Head + Missing Wagons + Remaining Tail + Misplaced Wagons
    fixed_train = head + missing_wagons + tail + misplaced_wagons
    
    return fixed_train


def add_missing_stops(routing_dict, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    sorted_stop_keys = sorted(stops.keys())
    
    ordered_stops = [stops[key] for key in sorted_stop_keys]
    
    routing_dict["stops"] = ordered_stops
    
    return routing_dict
        


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)

    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    fixed = [list(row) for row in zip(*wagons_rows)]

    return fixed
