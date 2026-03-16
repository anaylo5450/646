#!/usr/bin/env python3
import argparse,re
import pandas as pd
import matplotlib.pyplot as plt


def main(csv,top=8):
    df=pd.read_csv(csv,dtype=str)
    df["ZIP_CODE"]=df["ZIP_CODE"].astype(str)
    feb=[c for c in df.columns if re.fullmatch(r"total02_\d{2}_2022",c)]
    df["total"]=df[feb].apply(pd.to_numeric,errors="coerce").sum(axis=1)
    print(f"February 2022 days present in dataset: {len(feb)}")
    for _,r in df.sort_values("total",ascending=False).head(top).iterrows():
        print(f"{r['ZIP_CODE']:<8}{int(r['total']):>15}")
    for z in ["21532","21502"]:
        t=int(df.loc[df["ZIP_CODE"]==z,"total"].sum() or 0)
        print(f"{z:<8}{t:>15}")
    
    # Line graph for first 10 days of Feb 2022 for 20902 and 21502
    feb10=feb[:10]
    for z in ["20902","21502"]:
        row=df[df["ZIP_CODE"]==z].iloc[0]
        days=[int(c.split('_')[1]) for c in feb10]
        cases=[int(row[c]) for c in feb10]
        plt.plot(days,cases,label=z)
    plt.xlabel('Day of February 2022')
    plt.ylabel('Number of COVID Cases')
    plt.title('COVID Cases Comparison: First 10 Days Feb 2022')
    plt.legend()
    plt.savefig('feb2022_comparison.png')
    print("Graph saved as feb2022_comparison.png")


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("csv",nargs="?",default=r"c:\\Users\\mrcod\\Desktop\\646-1\\MD_COVID19_Cases_by_Zip_Code.csv")
    p.add_argument("-n",type=int,default=8)
    a=p.parse_args(); main(a.csv,top=a.n)
