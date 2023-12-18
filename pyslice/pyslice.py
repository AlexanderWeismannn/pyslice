import pandas as pd
import numpy as np
import os 


def slice(path: str | os.PathLike ,num_slices: int,res_fld: str = "res"):
    """
    Slice a given .csv file into a user specified number of smaller csv files.

    Args: 
        path (str or os.PathLike): path to the csv file.
        num_slices (int): number of slices to cut the .csv file into
        res_fld (str): name for the result folder where all split files will be stored
    Returns:
        No returns yet...    
    """

    #make res dir
    res_path = os.path.join(os.getcwd(),res_fld)
    os.makedirs(res_path)

    # split and file creation
    df = pd.read_csv(path)
    df_list = np.array_split(df,num_slices)
    count = 0
    for split in df_list:
        split.to_csv(f"{res_path}\\split_{count}.csv",index=False)
        count+=1

