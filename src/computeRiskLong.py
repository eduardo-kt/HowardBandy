# libraries
from datetime import datetime
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import random
from scipy import stats
import time


# set control variables
DD95_LIMIT: float = 0.20 
ACCURACY_TOLERANCE: float = 0.005
ISSUE: str = 'spy'
DATA_SOURCE: str = 'yahoo'
START_DATE: datetime = datetime(1999,1,1)
END_DATE: datetime = datetime(2012,1,1)
HOLD_DAYS: int = 5
SYSTEM_ACCURACY: float = .65
INITIAL_EQUITY: float = 1_00_000.0
FRACTION: float = 1.00
FORECAST_HORIZON: int = 504 # number of trading days in forecast horizon
NUMBER_FORECASTS: int = 10 # simulation runs

# Print Initial statements

print(f'''
    +----------------------------------------------+
    | Nem Simulation Run                           |
    | Testing Profit Potential for long Positions: |
    +----------------------------------------------+

Initial Equity:      {INITIAL_EQUITY}
Issue:               {ISSUE}
Period:
     from:           {START_DATE.strftime("%d %b %Y")}
     to:             {END_DATE.strftime("%d %b %Y")}
Holding Days:        {HOLD_DAYS}
System Accuracy:     {SYSTEM_ACCURACY:.2f}
Drawdown 95 Limit:   {DD95_LIMIT:.2f}
Forecast Horizon:    {FORECAST_HORIZON}
Number Forecasts:    {NUMBER_FORECASTS}
        ''')

# Get data

qt = yf.download(tickers= ISSUE, start= START_DATE, end= END_DATE, interval='1d', progress= False)

# Number of days in data
nrows = len(qt)

# Get Close prices
qtC = qt['Close']

# Get number of trades and number of days
number_trades = math.floor(FORECAST_HORIZON / HOLD_DAYS) # must be integer 
number_days = math.floor(number_trades * HOLD_DAYS) # must be integer

# Print  days in period, trades and trading days in forecast horizon
print(f'''
+----------------------------------------------------+
| Number of days in Period:\t\t\t{nrows} |
| Number of trading days in Forecast Horizon:\t {number_days} |
| Number of trades in Forecast Horizon:\t\t {number_trades} |
+----------------------------------------------------+
      '''
)

a1 = int(number_days + 1)
# these arrays are the number of days in the forecast
account_balance = np.zeros(a1) #account balance

pltx = np.zeros(a1)
plty = np.zeros(a1)

max_IT_DD = np.zeros(a1) # maximum intra-trade drawdown
max_IT_eq = np.zeros(a1) # maximum intra-trade equity

# These arrays are the number of simulation runs
# Max intra-trade drawdown

FC_max_IT_DD = np.zeros(NUMBER_FORECASTS)

# Trade equity (TWR)
FC_tr_eq = np.zeros(NUMBER_FORECASTS)

# ----------------------------------------
# Set up gainer and loser list

gainer = np.zeros(nrows)
loser = np.zeros(nrows)
i_gainer = 0
i_loser = 0

for i in range(0, nrows-HOLD_DAYS):
    if qtC.iloc[i+HOLD_DAYS]> qtC.iloc[i]:
        gainer[i_gainer] = i
        i_gainer = i_gainer + 1
    else:
        loser[i_loser] = i
        i_loser = i_loser + 1

number_gainers = i_gainer
number_losers = i_loser

print(f'Number Gainers:\t\t{number_gainers}')
print(f'Number Losers:\t\t{number_losers}')

#################################################
# Solve for fraction
fraction = 1.00
done = False

while not done:
    done = True
    print(f'Using fraction:\t\t{fraction:.3f}')
    # ---------------------------------
    # Beginning a new forecast run
    for i_forecast in range(NUMBER_FORECASTS):
    # Initialize for trade sequence
        i_day = 0 # i_day counts to end of forecast
        # Daily arrays, so running history can be plotted
        # starting account balance
        account_balance[0] = INITIAL_EQUITY
        # Maximum intra-trade equity
        max_IT_eq[0] = account_balance[0]
        max_IT_DD[0] = 0

        # for each trade
        for i_trade in range(0, number_trades):
            # select the trade and retrieve its index
            # into the price array
            # gainer of loser?
            # Uniform for win/loss
            gainer_loser_random = np.random.random()
            # pick a trade accordingly
            # for a long positions, test is "<"
            # for a short positions, test is ">"
            if gainer_loser_random < SYSTEM_ACCURACY:
                # choose a gaining trade
                gainer_index = np.random.randint(0, number_gainers + 1)
                entry_index = gainer[gainer_index]
            else:
                # choose a losing trade
                loser_index = np.random.randint(0, number_losers + 1)
                entry_index = loser[loser_index]

            # process the trade, day by day
            for i_day_in_trade in range(0, HOLD_DAYS+1):
                if i_day_in_trade==0:
                    # Things that happen immediately
                    # after the close of the signal day
                    # Initialize for the trade
                    buy_price = qtC.iloc[math.floor(entry_index)]
                    number_shares = account_balance[i_day] * fraction / buy_price
                    share_dollars = number_shares * buy_price
                    cash = account_balance[i_day] - share_dollars
                else:
                    # Things that change during a
                    # day the trade is held
                    i_day = i_day + 1
                    j = entry_index + i_day_in_trade
                    # Drawdown for the trade
                    profit = number_shares * (qtC.iloc[math.floor(j)]- buy_price)
                    MTM_equity = cash + share_dollars + profit
                    IT_DD = (max_IT_eq[i_day-1] - MTM_equity) / max_IT_eq[i_day-1]
                    max_IT_DD[i_day] = max(max_IT_DD[i_day-1], IT_DD)
                    max_IT_eq[i_day] = max(max_IT_eq[i_day-1], MTM_equity)
                    account_balance[i_day] = MTM_equity
                if i_day_in_trade == HOLD_DAYS:
                    # Exit at the close
                    sell_price = qtC.iloc[math.floor(j)]
                    # Check for end of forecast
                    if i_day >= number_days:
                        FC_max_IT_DD[i_forecast] = max_IT_DD[i_day]
                        FC_tr_eq[i_forecast] = MTM_equity
    # All the forecast have been run
    # Find the drawdown at the 95th percentile
    DD_95 = stats.scoreatpercentile(FC_max_IT_DD, 95)
    print(f'DD95: \t\t\t{DD_95:.3f}')

    if (abs(DD95_LIMIT - DD_95) < ACCURACY_TOLERANCE):
        # Close enough
        done = True
    else:
        # Adjust fracton and make a new set of forecasts
        fraction = fraction * DD95_LIMIT / DD_95
        done = False

# Report
# IT_DD_25 = stats.scoreatpercentile(FC_max_IT_DD, 25)
# IT_DD_50 = stats.scoreatpercentile(FC_max_IT_DD, 50)
IT_DD_95 = stats.scoreatpercentile(FC_max_IT_DD, 95)

print(f'DD95: \t\t\t{IT_DD_95:.3f}')

years_in_forecast = FORECAST_HORIZON / 252

TWR_25 = stats.scoreatpercentile(FC_tr_eq, 25)
CAR_25 = 100 * (((TWR_25/INITIAL_EQUITY) ** (1.0/years_in_forecast)) - 1.0)

TWR_50 = stats.scoreatpercentile(FC_tr_eq, 50)
CAR_50 = 100 * (((TWR_50/INITIAL_EQUITY) ** (1.0/years_in_forecast)) - 1.0)

TWR_75 = stats.scoreatpercentile(FC_tr_eq, 75)
CAR_75 = 100 * (((TWR_75/INITIAL_EQUITY) ** (1.0/years_in_forecast)) - 1.0)

print(f'CAR25:\t\t\t{CAR_25:.2f}')
print(f'CAR50:\t\t\t{CAR_50:.2f} ')
print(f'CAR75:\t\t\t{CAR_75:.2f}')

# Save equity curve to disc
np.savetxt('account_balance.csv', account_balance, delimiter= ',')

# Save CDF data to disc
np.savetxt('FC_maxIT_DD.csv', FC_max_IT_DD, delimiter= ',')
np.savetxt('FCTr.csv', FC_tr_eq, delimiter= ',')

# Plot maximum drawdown
for i in range(a1):
    pltx[i] = i
    plty[i] = max_IT_DD[i]
plt.plot(pltx, plty)
plt.show()
# end
