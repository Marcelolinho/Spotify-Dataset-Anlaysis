import pandas as pd
from pylab import *
from scipy import stats
import chardet as ch

def find_encoding(csv_file):
    with open(csv_file, 'rb') as f:
        result = ch.detect(f.read())
    return result['encoding']

encoding_found = find_encoding('./dataset.csv')

try:
    df = pd.read_csv('./dataset.csv', encoding = encoding_found)
    
    def streams_str_to_float(df):

        streams_str = df["Spotify Streams"].str.replace(",", "")

        streams_float = np.array([])

        for i in streams_str:
            if not isinstance(i, float):
                streams_float = np.append(streams_float, float(i)) 
            pass
        
        return streams_float
    
    mean_streams = round(streams_str_to_float(df).mean())
    streams_standard_deviations = round(streams_str_to_float(df).std())
    minimum_streams = round(streams_str_to_float(df).min())
    maximum_streams = round(streams_str_to_float(df).max())
    mode_streams = stats.mode(streams_str_to_float(df))

    def calculate_bins():
        ...

    print(f'Mean: {mean_streams}')
    print(f'Standard Deviation: {streams_standard_deviations}')
    print(f'Minimum Value: {minimum_streams}')
    print(f'Maximum Value: {maximum_streams}')
    print(f'Mode: {mode_streams}')
    
    bins = []

    dadosx = streams_str_to_float(df)

    fig, axes = plt.subplots(1, 1)

    axes.hist(dadosx, bins = bins,edgecolor = 'k')
    
    # fig.show()

except Exception as e:
    print(f'Erro de exceção {e}')

# plt.show()
