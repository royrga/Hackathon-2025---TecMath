import earthaccess
import xarray as xr

# This will work if Earthdata prerequisite files have already been generated
auth = earthaccess.login()

# To download multiple files, change the second temporal parameter
results = earthaccess.search_data(
    short_name="M2T1NXSLV",
    version="5.12.4",
    temporal=(
        "1980-01-01",
        "1980-01-01",
    ),  # This will stream one granule, but can be edited for a longer temporal extent
    bounding_box=(-180, 0, 180, 90),  # A tuple representing spatial bounds in the form
    # `(lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat)`
)

# Downlosd granules to local path
downloaded_files = earthaccess.download(
    results,
    local_path=".",  # Change this string to download to a different path
)

# OPTIONAL: Open granules using Xarray
ds = xr.open_mfdataset(downloaded_files)
print(ds)
