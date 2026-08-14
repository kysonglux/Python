import time
from datetime import datetime

epoch_seconds = time.time()

scientific_notation = "{:.2e}".format(epoch_seconds)

data_structure = datetime.utcfromtimestamp(epoch_seconds).strftime('%b %d %Y')
print(f"Seconds since January 1, 1970: {epoch_seconds:,.4f} or {scientific_notation} in scientific notation$")
print(f"{data_structure}$")