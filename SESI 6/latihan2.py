print("\n-----------------SESI 6-----------------")
print("06 - anindita k o - batch 002\n")
input("   klik enter untuk memulai")
print("-----------------------------------------------\n")

import numpy as np
import pandas as pd

r = pd.Series([5555,7000,1980])

print(r)
print(r.values)
print(r.index)

input("\n   klik enter untuk memulai\n")

city_revenue= pd.Series([5000, 6000, 7000], index=["Jakarta", "Bandung", "Yogyakarta"])
print(city_revenue)

input("\n   klik enter untuk memulai\n")

city_employee = pd.Series({"Jakarta":10, "Bandung":5})
print(city_employee)

input("\n   klik enter untuk memulai\n")

city_data = pd.DataFrame({"revenue":city_revenue, "employee":city_employee})
print(city_data)

input("\n   klik enter untuk memulai\n")

print(city_data.values)
