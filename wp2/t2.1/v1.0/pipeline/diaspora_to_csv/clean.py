import pandas as pd



# clean line break errors

def line_break(csv_files):
    
    for csv in csv_files:
        df = df.read_csv(csv)
        df = df.replace('\n','', regex=True)
        df.to_csv(csv)



# clean unescaped backslash

def unescaped_backslash(csv_files):
    
    for csv in csv_files:
        df = df.read_csv(csv)
        df = df.replace('\\\\','', regex=True)
        df.to_csv(csv)
