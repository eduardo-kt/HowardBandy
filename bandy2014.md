> Bandy, H. B. (2014). Quantitative technical analysis: An integrated approach to trading system development and trade management (1st edition). Blue Owl Press, Inc; bandy14.

**Quantitative Technical Analysis**<br>
_Howard Bandy_

# Chapter 01. Introduction
This book is about trading using quantitative techniques together with technical analysis.
* Our product will be a profitable trading system.
* Our process will be designing and verifying the system, them monitoring its performance and determining the maximum safe position size.
* Our metrics will be account growth, normalized for risk. 


The purpose of a trading system is to recognize an inefficiency in price, then make trades that capture that inefficiency. A trading system is a combination of a model and some data. The primary data series is a time-ordered sequence of prices of the issue being traded. The model is a logic which try to recognize patterns that precede profitable trading opportunities. 

A trading system is profitable as long as the logic applied to the data returns profit. That is, **as long as the logic and data remain synchronized.**. The logic of a typical trading system is relatively fixed while data is variable. **As the data changes, the patterns in the data move in and out of synchronization with the logic.** During periods of close synchronization, the system is healthy and large positions may safely be taken. As synchronization weakens, position size must be reduced. 

The output from the model is a list of trades for the time period being tested, together with a summary of performance. The list of trades, in time sequence, that results from processing a data series that is similar to future data, is the best estimate we can obtain of reality.

Trades can be categorized according to the amount of change from entry to exit, or the amount of time they are held. Over a period of time, there are only a few profitable trades for any given trade profile. Everyone developing systems that will hold trades for one to five days or one to two percent will locate the same profitable trades no matter what pattern or entry technique they are using. Every successful trade removes some inefficiency and makes future profitability less likely (**The markets are very nearly efficient**).

The trading system that results from the design, testing, and validation provides a single set of trades with single mean, single standard deviation, single terminal wealth, single maximum drawdown. These results will be repeated as the system is traded only if future prices are exactly the same as the historical series used during development. In order to estimate profit potential and risk it is important to consider the distribution of potential results.

The model does not include any position sizing - that is handled in trading management. The trading management sections of this book discuss a new and unique technique, _dynamic position sizing_, and introduce a new metric of system health, _safe-f_.

# Chapter 02. Risk and Risk Tolerance
Risk is the risk of drawdown in the balance of the account. The primary reason traders stop trading is that they experience a drawdown larger than they anticipated, larger than they can afford, larger than their risk tolerance.

## Measurement and Management
Measurement of risk and management of risk are related. Management is system design and position sizing. Measurement of risk helps us understand the tisk inherent with the combination of:
* the issue being traded
* accuracy of the trading system
* holding period
* intra-trade visibility

## Drawdown Defined
**Drawdown** is defined as the drop in account equity, measured as a percentage relative to the highest equity achieved prior to the drawdown. A system's equity is either at a new high, or it is in a drawdown. The gain needed to recover from a drawdown is greater than the loss that caused the drawdown. 

$$Drawdown=max \left( \frac{max\;equity-actual\;equity}{max\;equity},\;0\right)$$

Assume you are trading a system, it has an open long position, and the price of your issue is falling. What is the minimum period of time you are willing to hold through without taking a subjective action? One of the definitive aspects of using a quantitative sustem is that all of the rules are in the system. When the system issues a buy, a long position is taken, and it is held until the system issues a sell. So, the answer to "what is the minimum period of time you are willing to hold through" must be "until the system issues the exit". What does that imply?

Since drawdown can increase rapidly over a multi-day market decline, that period must be short enough that price changes, including drawdown, within it can be ignored. I recommend the minimum period between potential changes to position be no longer than one trading day.

> Drawdown é uma merda que cresce rápido. Então o sistema deve ser projetado para reavaliar as posições diariamente (ou menos tempo). 

## Maximum Adverse Excursion (MAE)
Maximum Adverse Excursion (MAE) is a measure of the most unfavorable point in a trade. MAE is a measure of risk we acknowledge. Similar to MAE, maximum favorable excursion (MFE) records the most favorable price. In a long trade, it is the highest high. **When using mark-to-market, whenever there is a new MFE and it establishes a new high for the account equity, adjust the equity to reflect that gain.**

$$MAE=max \left(\frac{entry-low}{entry},\;0\right)$$

Every trade has its own MAE, computed and reported daily. The accumulated drawdown spans trades and measures the highest marked-to-market bankable equity to lowest market-to-market equity. Your goal in trading the system is to determine the proper maximum safe position size, on a trade-by-trade basis, so the accumulated MAE rarely exceeds your risk tolerance. 

## Mark-to-Market Equivalence
From a mathematical perspective, the net equity change from a sequence of trades is identical whether the trades are considered as complete trades or as sequences of marked-to-market days. From a trading management perspective, marking-to-market daily gives finer resolution to the performance of the system and the opportunity to make subjectiv trading decisions, should they become necessary. From a trading system design perspective, marking-to-market daily transforms every system, no matter how often it buys and sells, into a system that has 252 daily results every year.

Although the trades extend over multiple days, the system design and system management focus is on the mark-to-market period - daily.

This does not imply changing positions every day. It does imply evaluating every day, and willingness to change positions daily. **In terms of changes to account equity and drawdown, an n-day trade is equivalent to n one-day trades**.

## Risk Tolerance

For a given set of trades, maximum drawdown is highly dependent on position size. There are many alternative methods of determining position size. **I recommend using fixed fraction as the position sizing technique**.

> Drawdown avalia a perda na conta de capital. MAE avalia a perda em um trade. O MAE é o drawdown aplicado ao trade. Através do position sizing convertemos o impacto do MAE em impacto de Drawdown. Se um determinado modelo tem mais chance de resultar em um grande MAE, então quanto maior o position sizing maior o risco de sofrer um grande drawdown. 

In terms of changes to account equity and drawdown, an n-day trade is equivalent to n one-day trades. From a trading sustem design perspective, marking-to-market daily transforms every system, no matter how often it buys and sells, into a system that has 252 daily results every year.

## Risk Tolerance
Every trader or trading company has a level of risk tolerance. It is the level of drawdown that, when reached or exceeded, causes the trader to accept that the system is broken and must be taken offline. Risk tolerance has four parameters:
* Account size (the initial balance)
* Forecast Horizon (how far into the future we look)
* Maximum Drawdown (level at which the system is taken offline)
* Degree of certainty 

A trading system was designed, coded, and tested using daily end-of-day data for the period 01/01/1999 through 01/01/2012. Validation (the test with out-of-sample data for generalization) produced a set of 506 trades for the 13 year period. That set of trades was used as the _best estimate_ of future performance. Assuming that future performance is similar to that of the best estimate, a two year forecast horzon will have about 78 trades. A monte carlo simulation was coded. 

## Position Size - safe-f
There many alternative methods of determining position size. I recommend using fixed fraction as the position sizing technique. For a given set of trades, maximum drawdown is highly dependent on position size. **Safe-f** is position size. It is recalculated after every trade and used to determine the size of the next trade. We simulate to estimate the position size related to desired maximum drawdown level and degree of certainty. 

# C03

# C04

# Chapter 05. Issue Selection

# Chapter 06. Model Development 
## Introduction
There are two approaches to trading system development:
* **Indicator-based:** compute an indicator, then observe price changes that follow.
* **Machine learning:** observe a notable price change, then identify patterns that precede.{ref}'target'

There are two modeling processes involved in trading system development: 
* **Developing the trading system:** it is developing the rules, identifying the patterns, analyzing the trades found in historical data, and validating the system.
* **Managing trading:** that is deciding whether the system is working or broken, and what size position is best for the next trade.

> _Developing or discovering high quality models is difficult. The markets are nearly efficient. Everyone is looking for the same profitables trades. Every profitable trade removes some of the inefficiency the system was designed to find._ 

## Aspects of Trading System Model Development
### Goal
The goal of the model - its sole purpose - is to identify profitable trades. Nothing else. 
### Pattern Recognition
Every series of trade prices is a combination of signals and noise. 

### Data
When daily data, often described as end-of-day data, is being used, one bar represents the trades made for an entire day.
### Trend Following
No matter which entry technique is used, no matter which patterns are found to be predictive, the trades sought are always trend following. To be profitable, the price at which the position is sold must be higher than the price at which it is bought.
### Indicators
Indicators can be based on anything. They are most useful when they have significant events, such as crossing or bottoms.
### Entries and Exits
A useful development practice is:
1. Identify the best entry point.
2. Identify he best exit point.
3. Evaluate the risk.
4. Evaluate the profit.
5. Explore patterns that precede entry and exit.
6. analyze results when either the entry or exit is not perfect.

```python
# zigzag function: True if Bottom. Buy signals.
z = zigzag(p, n)
Bottom[0] = 0
Bottom[-1] = 0
for i in range(1,len(Bottom) - 1):
    Bottom[i] = z[i] < z[i-1] and z[i] < z[i+1] # inverte para sell signals
```

The outline of the analysis:
1. Identify trades with daily prices: (Compute zigzag or some other indicator of your choice, Identify entry/exit, Identify trade and store it in an array.
2. Analyze performance. Using the array of trades, perform Monte Carlo analysis to assess risk, normalize for risk, determine safe-f, estimate profit, including CAR25.

This procedure defines an upper limit to profitability. 

### Trading Signals
* **Impulse signals** mark transitions, such as the beginning or end of a trade. Using impulse signals, one trade is one data point - however many days that trade lasts.
* **State signals** identify condiions (long, flat, or short). Using state signals, marking to market daily, each day is one data point. 

### Model Constraints
Much of the discussion among traders focuses on the definition of the pattern that signals the trades. People describe themselves, or their technique through themselves, as being trend following, mean reverting, seasonal, or pattern traders. To my thinking, we can develop better system if we relax our insistence that entries conform to particular categories. If we want the determining factor of systemm acceptability to be results, rather than the constraints, we must be willing to relax tradition-bound requirements.

### Fitting and Overfitting

> Accuracy refers to errors in missing the center of the target (between-sample error). Precision refers to the distance between shots (within-sample error). Overfitting can be defined as an overly precise solution to a general problem based on a limited sample. Overfitting s emphasizing precision over accuracy. 

The test of whether the model is properly fit or is overfit - whether it has learned or memorized - is testing with previously unseen data.

### Objective Function
In order to manage the fitting process, there must be an appropriate metric of goodness of fit that can be measured. For quantitative technical analysis, it is an objective function.

The purpose of the objective function is to provide a single-valued score for each alternative, where the ranking of the alternatives is in the same order as our subjective preferences.

>_We are using the objective function to quantify subjectivity._

The best alternative, seem from trading results, is subjective. It includes positive growth of the trading account, limited drawdowns to the trading account, and conformity of results to real or artificially imposed constraints such as trading frequency and holding period.

> _CAR25 is the credible value of expected equity growth associated with the risk-normalized forecast of a trading system. It is the most universal objective function for trading system development and trading management I have found._

What characteristics of the series of trades give high CAR25?
* trade frequently
* trade accurately
* hold a short period
* have a high gain per trade
* penalize drawdown (specially large losses)

### Backtesting
A backtest is an evaluation of a system using data previously collected - historical data. 

### Optimization
The optimization is a search through a search space. Each indicator (or other feature being searched) defines a dimension in a seach space. We are searching for the highest stable area of that surface.

If run times are acceptable, use exhaustive search. Check for spikes in the response surface. Preferred solutions are located in "plateaus" with smooth slopes. 
>_Do not obsess over perfection. A good local optimum may be satisfactory. Prefer a robust system with lower performance to a fragile system with higher performance._

### Stationarity and Synchronization
To be profitable, a system must:
* learn the predictive patterns by analysis of the training data.
* identify those patterns in the validation data, and eventully in live-trading data.

Training data is in-sample data. Validation data is out-of-sample data.

Stationarity is a feature of data that refers to how a particular metric of the data remains relatively constant or changes as different subsets of the data are analyzed.

The trading system - the combination of model and data - is not stationary. Applying techniques that are appropriate for stationary processes to models that are not stationary produces inaccurate and unreliable results. 

The signal or pattern component of the data must be stationary thoughout the in-sample traning period. The in-sample period may be shorter than the period of synchronization, but avoid longer periods. The issue is not the length of the period in days so much as it is the length of the period of stationarity.

Naive developers are sometimes heard to recommend using as much data and as long a period as possible for each test period. Their reasoning is that the model will be exposed to as many different conditions as possible and will be able to perform well in all of them. My view is quite the opposite. I recommend that the test periods - particularly the in-sample periods over which the model is fit to the data - be as short as practical. Using data that includes an different conditions decreases the fit to an of the conditions. 

In my opinion, there is no minimum length for the out-of-sample period. It is, or at least can be, appropriate to treat each day as a one-day long out-of-sample period, with parameter values readjusted daily. 

In general, the lengths of the in-sample and out-of-sample periods are related only to the extent that the system must remain synchronized for the total length of those two periods. 

One thing you can expect is that longer holding periods require longer periods of stationarity in order to indentify and vlaidadte signal recognition. That implies boh longer in-sample periods, and longer out-of-sample periods. Increasing the length of time increases the probability that conditions change, stationarity is lost, and profitability drops. 

Additionally, drawdown increases as holding period increases. Longer holding periods imply greater risk, smaller safe-f, and lower CAR25.

Again, we have a familiar tradeoff. We want more data points for finer granularity, better precision, and easier statistical significance. But not so many data points that some of them represent conditions that are no longer current. 

Each data point is a trade that is both opened and closed within the test period. The longer positions are held, the longer the test period must be to span several trades; and the greater the intra-trade drawdown.

> The longer the test period, the more likely the model and the data will lose synchronization. 


### Validation

The gold standard of validation is walk forward testing. 

WF is a sequence o steps. Each step consists of finding the best model using the in-sample data, then using that model to test the out-of-sample data. The search for the best model is an optimization. You do not have an opportunity to evaluate the top choice. The optimization is applied to in-sample then the selected model is applied to out-of-sample data and stored. This process is repeated several times. After each step, the beginning and ending dates of both periods are stepped forward by the length of the out-of-sample period. 

The results from all of the out-of-sample tests are accumulated and analyzed. The decision to pass to real trading is based on analysis of these trades. 

After passing to real trade, the process continues. Periodically, either according to the walk forward schedule, or whenever trading results are deteriorating, resynchronize the model to the data using the same process. 

#### These conditions are required for walk forward to work:
* the suystem is stationary for the combined length of the insample and out-of-sample periods.
* you are confident that the model selectedby your objective function as best based on in-sample optimization.
* There are several, preferably many, trades in each test period. 

### Some Other Way
If satisfactory walk forward results cannot be obtained, weaker validation techniques can be used:
* testing on other data series.
* testing on earlier time periods (weak technique)

## Next Chapters
There is a logical sequence of operations that model development follows:
* set goal and performance metrics
* choose the primary data series
* choose auxiliary data series
* date and time align the data series
* select and compute functions and indicators
* select the target
* reduce dimensions or change basis
* determine lengths of in-sample and out-of-sample periods
* learn
* test
* evaluate performance
* predict and trade

# Chapter 07. Model Development Indicator Based

## Objective Function
One of he first steps in indicator-based development is choice of the objective function. It must encapsulates and quantifies the subjective preferences of the developer, and assign a single-valued score to each set of trades evaluated (reward desirable characteristics and penalize underirable characteristics).

Important metrics to use in objective functions:
* Percentage gained per trade.
* Number of bars held.
* Number of trades per year.
* Percentage of trades that are winners.
* Percentage of time a position is held.
* Magnitude of losing trades.

Because **they are sequence dependent**, these metrics should be avoided:
* Maximum drawdown for the test period.
* Maximum losers in a row.
* Time between new highs.

> If available, CAR25 would be the preferred objective function.

You can use **'decathlon'** scoring: select, compute, scale, then add or multiply the metrics.

## Select Data Series
Begin with those series that jave passed the risk and profit screen, are very liquid, and easily traded. Prefer those with high safe-f scores and high CAR25 scores. You can use any data series you want, but is easier to develop profitable, safe, tradable system with those characteristics.

## System Overview
While there may be a short/flat system for the same data series, I recommend developing long/flat separately first because:
* It is easier to identify bottoms and entries for long trades than tops and entries for short trades.
* Long/flat has fewer rules and parameters than long/flat/short.
* There is an upward bias in price related to factors such inflation, population growth, and productivity increase that favor being long equities.
* The characteristics of profitable long trades and profitable short trades are different for most issues. If a short/flat system does exist, it is probably not a reversal or symmetrical system.

## Indicator Selection
* We expect there about 15 to 50 ideal trades per year. To pick a specific number for discussion, say 24 trades per year.
* Signals generated by indicators are crossings or turnings. One indicator crosses another indicator, an indicator crosses a critical level, an indicator changes direction, or something similar.
* The indicator cycle must fit to price data and generates the desirable number of trades. For the trades we hope to identify, choosing a loockback (period between buy and sell) that is shorter than ideal (for example, to identify 24 trades in a year, the lookback period must be about 10 days) is more forgiving than choosing one that is longer than ideal. 
### Chart Patterns
Patterns in the sequence and relationship of OHLC for a few bars are easily identified and sometimes reliably precede price changes (for example, three consecutive higher closing prices are often followed by a fall in prices). Be aware that patterns are highly susceptible to overfitting.   

## Discovering Tradable Systems
There is some subjectivity, and it will require some experimentation on your part, to determine the best lengths to use for in-sample and out-of-sample periods. Try one year out-of-sample and 1-6 year in sample periods. Adjust as you learn the characteristics of the system. The lengths that work depend on the strength of the trading signal within the data's noise, stationarity of the signal, and robustness of the model to changes in synchronization.

## Summary
* Develop a statement of personal risk tolerance.
* Analyze potential data series to determine the risk and profit potential in each. 
* Using relatively simple entry rules, develop and backtest a series of odels to see if those issues have profitable trades that follow persistent patterns.
* Using an objective function to rank alternative systems, use the walk forward process to objectively choose systems.
* The final result is a set of trades, produced as objectively as possible, that are the best estimate of future performance of the system. 

# Chapter 08. Model Development Machine Learning

# Chapter 09. Trading Management

# Chapter 10. Summary and Random Thoughts
* Abandon Financial Astrology
* Become a competent programmer
* Bad data is worse than no data
* Think probabilistically
* Forecasts can change (improve with experience and new information)
* A simple algorithm with refined data usually outperforms a complex algorithm with raw data
* Trading systems are like blackjack. There is a model that works under some conditions
* Learn the mathmatics
* Nothing about financial data or trading systems is stationary.
* There are no physical laws governing the behavior of financial markets. If there were, new information would not matter much, and there would be little profit opportunity.
* Quantify your risk tolerance.
* The system results in an equity curve. Analysis of the equity curve determines the goodness of the system. That is, what is the terminal wealth and what is the drawdown.
* Financial data does not follow Normal distribution. Do not assume that it does, nor try to force it to be, nor naively use techniques that assume Normality.
* When you have enough, Quit. There is always a non-zero probability of an account destroying black swan event.

# Bibliography
Downey, A. B. (2015). Think Stats: Exploratory data analysis (2. ed). O’Reilly.

Downey, A. B. (2021). Think Bayes: Bayesian statistics in Python (Second edition). O’Reilly.

Gigerenzer, G. (2002). Calculated risks: How to know when numbers deceive you. Simon & Schuster.

Haigh, J. (2003). Taking chances: Winning with probability. Oxford University Press.

Silver, N. (2021). O sinal e o ruído. Intrínseca; silver21.

Stone, J. V. (2014). Bayes’ rule: A tutorial introduction to Bayesian analysis (First edition, third printing [with corrections]). Sebtel Press.

Connors, L. A., & Alvarez, C. (2012). How markets really work: A quantitative guide to stock market behavior (Second edition). John Wiley & Sons, Inc.








[def]: 41