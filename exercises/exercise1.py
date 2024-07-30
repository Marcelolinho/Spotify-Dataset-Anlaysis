import pandas as pd
from pylab import *
import chardet as ch

def find_encoding(csv_file):
    with open(csv_file, 'rb') as f:
        result = ch.detect(f.read())
    return result['encoding']

try:
    encoding_found = find_encoding('./dataset.csv')

    df = pd.read_csv('./dataset.csv', encoding = encoding_found)

    print(df.describe())

    print(f'Spotify Streams Missing: {df['Spotify Streams'].isna().sum()}')

    def calculate_streams_mean(df):

        streams_str = df["Spotify Streams"].str.replace(",", "")

        streams_float = np.array([])

        for i in streams_str:
            if not isinstance(i, float):
                streams_float = np.append(streams_float, float(i)) 
            pass
        
        return np.mean(streams_float)

    media_streams = calculate_streams_mean(df)

    df['Spotify Streams'].fillna(media_streams, inplace = True)

    print(f'\nValues filled with stream mean: {media_streams}')
    print(f'Spotify Streams Missing: {df['Spotify Streams'].isna().sum()}')
    
except Exception as e:
    print(f'Erro de exceção: {e}')
