import pandas as pd 
def calculate_average(df):
    df['Average']=df[['Python','DSA','Maths']].mean(axis=1)
    return df

def subject_average(df):
    return df[['Python','DSA','Maths']].mean()

def top_students(df, n=5):
    return df.sort_values('Average', ascending=False).head(n)