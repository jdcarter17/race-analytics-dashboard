import pandas as pd

def participation_by_gender(data):
    return data.groupby("gender").size()