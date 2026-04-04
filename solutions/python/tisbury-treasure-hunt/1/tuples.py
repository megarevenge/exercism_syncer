"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    return tuple(azara_record[1]) == tuple(rui_record[1])


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    # Unpack Azara's data
    treasure, azara_coord = azara_record
    
    # Unpack Rui's data
    location, rui_coord, quadrant = rui_record
    
    # Re-format Rui's tuple ('4', 'B') into a string '4B' for comparison
    combined_rui_coord = rui_coord[0] + rui_coord[1]
    
    if azara_coord == combined_rui_coord:
        return (treasure, azara_coord, location, rui_coord, quadrant)
    
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = ""
    
    for record in combined_record_group:
        
        cleaned_record = (record[0], record[2], record[3], record[4])
        
        report += str(cleaned_record) + "\n"
        
    return report
