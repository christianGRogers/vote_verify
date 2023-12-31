from constants import (SEP, IN_ED_CODE, IN_ED_NAMEE, IN_POPULATION, 
                       DIST_POP, DIST_NUM, DIST_FILE_NAME, FILE_TYPE, 
                       VOTE_FILE_NAME, CANADATE_END, CANADATE_START)
from typing import TextIO

def main() -> None:
    """Program start point"""
    district_file = open(DIST_FILE_NAME+FILE_TYPE)
    districts = get_district(district_file)
    district_file.close()
    region_code_to_canadate_votes = get_stations(districts)
    print(region_code_to_canadate_votes)

def get_stations(districts) -> dict[str, dict[str,int]]:
    """Return region code to canadate names to votes; from districts 
    nameing patterened files
    """
    district_to_canadates_votes = {}
    for district in districts:
        current_vote_file = open(VOTE_FILE_NAME+district[DIST_NUM]+FILE_TYPE)
        district_to_canadates_votes[district[DIST_NUM]] = count_district(current_vote_file)
    return district_to_canadates_votes


def count_district(data_file: TextIO) -> dict[str:int]:
    """Return all the canadates in data file to their respective vote
    count in the region
    """
    canadates = data_file.readline().split(SEP)[CANADATE_START:CANADATE_END]
    canadates_to_votes = {}
    votes = []
    for canadate in canadates:
        canadates_to_votes[canadate] = 0
    for line in data_file:
        votes.append(line.split(SEP)[CANADATE_START:CANADATE_END])
    for vote in votes:
        i = 0
        for canadate in canadates_to_votes:
            canadates_to_votes[canadate] += vote[i]
            i += 1
    return canadates_to_votes


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


