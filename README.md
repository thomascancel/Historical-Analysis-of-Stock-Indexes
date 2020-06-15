# Historical-Analysis-of-Stock-Indexes
In this project I study historical performance of the S&P500 Index over the last 50 years and the last 12 months. The data is extracted directly from yahoo finance which makes it easy to update the graphs every day. A similar analysis can be done for different indexes or stocks just by changing the ticker in the json file.

## Requirements
Here are the versions of the librairies I used for this project.

* Python 3.7
* Pandas 1.0.3
* Numpy 1.18.2
* yfinance 0.1.54
* Matplotlib 2.2.2

## Results

### Annual Analysis

![alt text](https://github.com/thomascancel/Historical-Analysis-of-Stock-Indexes/blob/master/results/S&P_500_historical_50Y_returns.png?raw=true)

Between 1970 and 2019, the Total Annual Return of the S&P 500 has been positive 39 years and negative 11 years. Negative peaks are often caused by global crises, as was the case in 1974 with the oil crisis or in 2008 with the financial crisis.

![alt text](https://github.com/thomascancel/Historical-Analysis-of-Stock-Indexes/blob/master/results/S&P_500_histogram_50Y_returns.png?raw=true)

As seen previously, the Total Annual Returns of the S&P 500 have been mostly positive (78% of the time). For 24% of cases they were even above 20%.

### Monthly Analysis

![alt text](https://github.com/thomascancel/Historical-Analysis-of-Stock-Indexes/blob/master/results/S&P_500_historical_12M_returns.png?raw=true)

A similar monthly study may also be carried out. For this I have considered the last 12 months from the moment I have published this project (from July 2019 to June 2020). Thus the impact of the covid-19 crisis can be observed. Indeed, the sharp fall during the months of February and March is clearly visible with a minimum of almost -10%. The month of April was marked by a sharp rise (+13%).

![alt text](https://github.com/thomascancel/Historical-Analysis-of-Stock-Indexes/blob/master/results/S&P_500_histogram_12M_returns.png?raw=true)

This histogram is also showing us the impact of the covid-19 crisis. The months of February and March had returns between -10% and -5% and the month of April a return between 10% and 15%.
