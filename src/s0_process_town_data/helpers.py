import glob
import os
import re

import geopandas as gpd


def process_town_data():
    """
    https://data.gov.tw/dataset/7441
    """
    raw_path = "data/raw/town"
    processed_path = "data/processed/town"
    town_v = os.listdir(raw_path)[-1]
    date_v = re.findall(r"\d+", town_v)[0][2:8]
    file_path = glob.glob(f"{raw_path}/{town_v}/TOWN_MOI_*.dbf")[0]

    town_gdf: gpd.GeoDataFrame = gpd.read_file(file_path, encoding="utf-8")
    town_df = town_gdf[["COUNTYCODE", "TOWNCODE", "COUNTYNAME", "TOWNNAME"]]

    if not os.path.exists(processed_path):
        os.mkdir(processed_path)

    town_df.to_csv(f"{processed_path}/town.csv", index=False)
    town_df.to_csv(f"{processed_path}/town_{date_v}.csv", index=False)
