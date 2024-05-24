import func

def main() -> None:
    """Program start point"""
    district_file = open(DIST_FILE_NAME+FILE_TYPE)
    districts = get_district(district_file)
    district_file.close()
    region_code_to_canadate_votes = get_stations(districts)
    canadate_file = open(CANADATE_FILE_NAME)
    canadate_to_political_afil = get_canadates_to_political_afil(canadate_file)
    canadate_file.close()
    print(verify_winner(canadate_to_political_afil, region_code_to_canadate_votes))
