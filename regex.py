# regex.py

RAW_DATA_FILES_PATH = "G:\\My Drive\\AirPollutionML\\Raw_Data_Files"
"""str: Raw data file's directory absolute path"""

STATION_FILE_PATTERN = r"(\d{4})_([A-Za-z]+)_([A-Za-z0-9-]+)\.csv"
"""str: Regex pattern for files of each station from source"""

YEAR_REGION_FILE_PATTERN = r"(\d{4})_([A-Za-z]+)\.csv"
"""str: Regex pattern for files of each year by each region with mean of station data"""

YEAR_ALL_REGION_FILE_PATTERN = r"(\d{4})_all_regions\.csv"
"""str: Regex pattern for files of each year and all regions as column"""

REGION_ALL_YEAR_FILE_PATTERN = r"([A-Za-z]+)_all_years\.csv"
"""str: Regex pattern for files of each region with all years"""

YEAR_FILE_PATTERN = r"(\d{4})\.csv"
"""str: Regex pattern for files of each year with mean of all regions"""
