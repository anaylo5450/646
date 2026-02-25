import re
import pandas as pd
import matplotlib.pyplot as plt

zipdf = pd.read_csv('Zip_Code_Lookup_Table.csv', usecols=["ZipCode","County"])

# detect any county names containing characters other than letters or whitespace
pattern = re.compile(r'[^A-Za-z\s]')
special_counties = [c for c in zipdf['County'].unique() if pattern.search(c)]
if special_counties:
    print("\nCounties with special characters:")
    for c in special_counties:
        print(f"  {c}")
else:
    print("\nNo county names contain special characters.")

# calculate and print the requested statistics
# assuming the CSV contains only Maryland entries
distinct_zips = zipdf['ZipCode'].nunique()
distinct_counties = zipdf['County'].nunique()
print(f"Distinct ZIP codes in Maryland: {distinct_zips}")
print(f"Distinct counties in Maryland: {distinct_counties}")

# compute number of ZIP codes for each county
ZipCodesByCounty = (
    zipdf.groupby('County')['ZipCode']
         .count()
         .reset_index(name='NumOfZipCodes')
         .sort_values(['NumOfZipCodes'], ascending=False)
)

# explicitly re-sort to guarantee descending order before printing
ZipCodesByCounty = ZipCodesByCounty.sort_values('NumOfZipCodes', ascending=False)

# display only the top 10 counties by ZIP code count
print("\nTop 10 counties with the most ZIP codes:")
print(f"{'County':>40}{'NumOfZipCodes':>10}")
for _, row in ZipCodesByCounty.head(10).iterrows():
    print(f"{row['County']:>40}{row['NumOfZipCodes']:>10}")

# lookup for Allegany County
allegany_count = ZipCodesByCounty.loc[ZipCodesByCounty['County'].str.contains('Allegany', case=False), 'NumOfZipCodes']
if not allegany_count.empty:
    print(f"\nZIP codes in Allegany County: {int(allegany_count.iloc[0])}")
else:
    print("\nAllegany County not found in dataset")

# add running total and simplified county name for plotting
ZipCodesByCounty['RunningTotal'] = ZipCodesByCounty['NumOfZipCodes'].cumsum()
ZipCodesByCounty['County Name'] = ZipCodesByCounty['County'].map(lambda x: re.sub(r'County$|City$','',x).strip())

# plot the running total
ZipCodesByCounty.plot(x='County Name', y='RunningTotal', kind='line',
                       style='yo-', label="Running Total", fontsize=8)
plt.xticks(rotation='vertical')
plt.ylim(bottom=0)
plt.title("Running Total Of MD Zipcodes", y=1.05, fontsize=11)
plt.ylabel("Number of MD Zipcodes",labelpad=15)
plt.xlabel("MD County",labelpad=15)
plt.legend()
plt.show()