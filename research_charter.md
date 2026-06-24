# Research Charte: Options-Informed Systematic Equity Research Platform

##Core Hypothesis 
Tradition cross- sectional alpha factors( Value, Momentum, Quality, Revisions) yield superior out-of-sample risk-adjusted performance, lower max drawdowns, and better tail-risk profiles when dynamically conditioned on forward-looking option-implied risk chacteristics ( Volatitilty Risk Premium, Put-Call Skew, Term Structure).

## 2. Investment Universe and Boundaries
* **Asset Class:** US Liquid Common Equities (CRSP share codes 10 and 11) 
* **Optionable Filter:** Restricted strictly to underlying securities with active, liquid option chains inside OptionMetric IvyDB US.
* **Liquidity Screens:** Exclude Penny stocks ( price < $5) and securites below the 20th percentile of rolling 21-day Average Daily Dollar Volume (ADDV)
* **Rebalancing Frequency:** Monthly (Calander-driven, Signals are formed using data available after the close of the final trading day of month t. Portfolios are executed at the next trading day’s close/open, depending on available price assumptions.)

## 3. Data Splits & Regiime Testing 
To prevent lookahead and data-mining bias, the historical data panel will be cleanly bbisected into distinct operational periods:
* **In-Sample Estimation/Train Window:** [e.g., January 2005 - December 2016]
    * *Purpose:* Signal engineering, factor neutralisation calibration and baseline rtegression fitting
* **Out-of-Sample Test WWindow:** [e.g., january 2017 - December 2025]
    * *Purpose:* Isolated walk forward testing. No parametes may be tuned using this data. Must span distinct regimes (e.g., 2018 Volatility Spike, 2020 Covid Crash, 2022 Rate Hikes)

## 4. Signal Architecture
### A. Equity Baseline Features (The physical World)
* **Momentum (CRSP):** 12-minus-1 month cumulative log returns
* **Short-Term Reversal (CRSP):** Previous 5-day log retuens 
* **Value(Compustat):** Book-to-Market Ratio ( appropriately lagged by 3-6 months to avoid publication lookahead bias)
* **Quality (Compustat):** Return on equity (ROE) residualised against leverage proxies 
* **Revisions (I/B/E/S):** 30-day change in concesus forward EPS analyst estimates

### B. Options Conditioning Features (The Risk-Neutral World)
* **Implied Volatility (OptionMetrics):** 30-day at-the-money (ATM) implied volatility
* **Volatility Risk Premium (VRP):** 30-day ATM Implied Volatility minus rolling 21-day historical raliszed volatility
* **Put-Call Skew:** Implied volatility of 25-delta puts minus 25-delta calls
* **Term Structure:** 91-day ATM Implied volatility misnus 30-day ATM implied volatility 

## 5. Target Variable
* **Definition:** 21-day forward excess return relative to cap weighted universe benchmark ($R_{t \rightarrow t+21} - R_{bench}$)

## 6. Realism & Cost constraints 
* **Equity Transaction Costs:** Assumed flat penalty of 5 basis points (bps) per one way trade to account for execution slippage and standard institutional commissions
* **Option Liquidity Filters:** Underlyinf entitites are automatically rejected if their corresponding option chain exhibits an average bid-spread ask wider than $X\%$ or zero open interst in the front two expiry months

## 7. Hard Rejection Criteria (Falseification Rules)
The options-informed conditioning layer will be formally **REJECTED** and devlared a failuse if any of the following conditions trigger out-of-sample:
1. The Options-Informed Model does not beat the Equity-Only Model's out of sample sharpe ratio by at least 0.15
2. The apparent out-of-sample slpha disappears completely after residualising the portfolios weight agains standard style factors ( Market Beta, Size, Volatility)
3. The strategy's turnover increases to a point where net transacttion costts entirely absorb gross outtperformace
4. The strategy's performace gains are entirely concentrated within illiquid microcap names where executing trades is fundamentally unfeasible