from constants import (SEP, IN_ED_CODE, IN_ED_NAMEE, IN_POPULATION, 
                       DIST_POP, DIST_NUM, DIST_FILE_NAME)
from typing import TextIO

def main() -> None:
    """Program start point"""
    district_file = open(DIST_FILE_NAME)
    districts = get_district(district_file)
    

def get_stations(data_file: TextIO, districts) ->: #sumtin
def get_district(data_file: TextIO) -> dict[str,dict[str, int]]:
    """Return a district names from data_fil mapping to corosponding 
    district numbers and voting populations indicated by constants 
    DIST_NUM and DIST_POP.

    Preconditions: data_file is open for reading with cursor at start position
    data file is of oficial format given by elections.ca
    """
    line = data_file.readline() #skip first line
    districts = {}
    for line in data_file:
        line = line.strip().split(SEP)
        districts[line[IN_ED_NAMEE]] = {DIST_POP: line[IN_POPULATION], 
                                        DIST_NUM: line[IN_ED_CODE]}
    return districts

main()


