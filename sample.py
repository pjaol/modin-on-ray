import ray
ray.init(address="auto")

import modin.pandas as pd

@ray.remote(scheduling_strategy="SPREAD")
def download_data():
    import urllib
    urllib.request.urlretrieve("https://data.lacity.org/api/views/6rrh-rzua/rows.csv?accessType=DOWNLOAD", 'businesses.csv')
    return 'businesses.csv'

obj_rt = [download_data.remote() for _ in range(3)]
ray.get(obj_rt)
df = pd.read_csv("businesses.csv")
df[df["BUSINESS NAME"].str.contains("IN-N-OUT BURGER", na=False)]