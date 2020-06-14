import os
import json
import pandas as pd
from Extract_data import Extraction
from Data_analysis import Data_analysis


def main():
    configs = json.load(open('config.json', 'r'))
    if not os.path.exists(configs['data']['save_dir']): os.makedirs(configs['data']['save_dir'])
    if not os.path.exists(configs['analysis']['save_results']): os.makedirs(configs['analysis']['save_results'])

    # To extract data from Yahoo finance
    Extraction(configs['data']['ticker'], configs['data']['column'],
               configs['data']['save_dir']).get_historical_data_50Y(
        configs['data']['start_date'], configs['data']['end_date'])
    Extraction(configs['data']['ticker'], configs['data']['column'],
               configs['data']['save_dir']).get_historical_data_1Y()

    # Read csv files
    data_12M = pd.read_csv(os.path.join(configs['data']['save_dir'], 'data_1Y.csv'))
    data_50Y = pd.read_csv(os.path.join(configs['data']['save_dir'], 'data_50Y.csv'))

    # Make analysis
    data = Data_analysis(data_50Y, data_12M, configs['analysis']['save_results'])
    data.plot_annualized_returns()
    data.histogram_annualized_returns()


if __name__ == '__main__':
    main()
