Absolutely — here is the **minimum viable but still very impressive** version, plus the matching **research charter** in full markdown.

This version keeps the mathematical finance core, but cuts the scope down to something you can actually finish and defend well. It still uses the same institutional data stack you have access to through WRDS, including CRSP, OptionMetrics IvyDB US, Compustat, and I/B/E/S.    

---

# `research_charter.md`

````md
# Research Charter: Volatility Surface Research Lab

## From Stochastic Pricing to Cross-Sectional Alpha

---

## 1. Project Title

**Volatility Surface Research Lab: From Stochastic Pricing to Cross-Sectional Alpha**

Repository name:

```text
vol-surface-alpha-lab
````

Alternative CV title:

```text
Options-Implied Risk and Equity Alpha Research Platform
```

---

## 2. One-Sentence Summary

This project builds a small but serious mathematical finance and empirical research platform that implements stochastic process simulation, option pricing, implied-volatility inversion, and simple volatility-surface construction from first principles, then applies those tools to real option-chain and equity data to test whether mathematically derived option-surface features improve volatility forecasting, cross-sectional equity selection, drawdown control, and portfolio construction.

---

## 3. Core Research Motivation

Traditional systematic equity research uses signals such as momentum, value, quality, analyst revisions, volatility, and liquidity to forecast future stock returns. Mathematical finance and derivatives research, on the other hand, studies how option prices encode expectations about volatility, skew, tail risk, and hedging costs.

This project is motivated by the idea that these two worlds should not be treated separately.

The options market contains forward-looking information about uncertainty and downside protection. A traditional equity signal may look attractive in isolation, but its usefulness may depend on the level of risk being priced in the options market.

Examples:

* A stock may have strong momentum but extreme downside skew.
* A value stock may look cheap but have expensive implied volatility.
* A quality stock may have stable fundamentals and relatively cheap implied volatility.
* A high-revision stock may already have uncertainty fully priced into its options.
* A portfolio may have positive expected alpha but hidden exposure to volatility shocks, skew, liquidity, or crash risk.

The central aim of this project is therefore to derive simple option-implied risk features from first principles and test whether they improve empirical equity and volatility research.

---

## 4. Core Research Question

Can option-surface quantities derived from first-principles pricing models improve volatility forecasting, cross-sectional equity selection, drawdown control, and portfolio risk control beyond traditional equity signals and vendor-provided option fields?

---

## 5. Main Hypotheses

### H1: Volatility Forecasting Hypothesis

Option-surface features derived from cleaned option chains predict future realized volatility better than historical realized volatility alone.

Examples of relevant features:

```text
ATM implied volatility
volatility risk premium
term structure slope
simple skew measures
option liquidity
```

---

### H2: Tail-Risk Hypothesis

Simple risk-neutral or skew-based option features contain useful information about future drawdowns and negative return events.

Examples of relevant features:

```text
risk-neutral skewness proxy
left-tail probability proxy
put-call skew
option-implied volatility
term structure
```

---

### H3: Surface-Derived Feature Hypothesis

Self-derived option features add information beyond simple vendor-provided option fields such as ATM implied volatility, raw skew, option volume, and open interest.

The key comparison is:

```text
vendor options fields
vs
self-derived implied volatility / skew / VRP
```

---

### H4: Equity Signal Conditioning Hypothesis

Traditional equity signals such as momentum, value, quality, and analyst revisions perform differently depending on the option-implied risk environment.

Examples:

```text
momentum × implied volatility
value × downside skew
quality × volatility risk premium
analyst revisions × option-implied uncertainty
```

---

### H5: Practical Robustness Hypothesis

Any apparent benefit from option-surface features must survive realistic implementation assumptions, including liquidity filters, transaction costs, point-in-time data alignment, sector and factor risk controls, and out-of-sample validation.

---

## 6. What This Project Is

This project is a combined mathematical finance and systematic research platform.

It has two connected halves:

```text
Half 1:
Build the mathematical machinery.

Half 2:
Use the machinery in real empirical research.
```

The mathematical machinery includes:

```text
stochastic process simulation
option pricing
Greeks
implied-volatility inversion
simple volatility-surface construction
delta-hedging simulation
```

The empirical research layer includes:

```text
CRSP equity returns
OptionMetrics option chains
Compustat fundamentals
I/B/E/S analyst revisions
equity signals
option-surface signals
volatility forecasting
cross-sectional return prediction
tail-risk filtering
portfolio construction
transaction costs
attribution
robustness testing
```

---

## 7. What This Project Is Not

This project is not:

```text
a trading bot
a copied Black-Scholes calculator
a yfinance backtester
a pairs-trading notebook
a generic factor backtest
a random ML-on-stock-prices project
a dashboard pretending to be research
a project that blindly trusts vendor option fields
```

Black-Scholes is only the baseline. The actual project is the option-pricing, implied-volatility, and empirical research pipeline built on top of it.

---

## 8. Research Scope

The project focuses on US listed equities with available option-chain data.

The research will test three broad empirical applications:

1. **Volatility forecasting**

   * Can option-surface features predict future realized volatility?

2. **Cross-sectional equity selection**

   * Can option-surface features improve a traditional equity alpha model?

3. **Risk and portfolio control**

   * Can simple option-implied tail-risk measures reduce drawdowns or improve position sizing?

The project may also include a small hedging-error study.

---

## 9. Data Sources

### 9.1 Core Data Sources

| Data Need                       | Source                                          | Purpose                                                                     |
| ------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------- |
| Stock prices                    | CRSP                                            | Daily prices, returns, realized volatility, momentum, backtest returns      |
| Stock volume                    | CRSP                                            | Liquidity filters, ADV, transaction cost proxies                            |
| Delisting returns               | CRSP                                            | Survivorship-bias control                                                   |
| Share codes and exchange codes  | CRSP                                            | Common-stock universe construction                                          |
| Market capitalization           | CRSP / Compustat                                | Size signal, liquidity screen, universe ranking                             |
| Fundamentals                    | Compustat                                       | Value, quality, profitability, leverage                                     |
| Analyst forecasts and revisions | I/B/E/S                                         | Analyst revision signal, forecast dispersion, analyst coverage              |
| Option chains                   | OptionMetrics IvyDB US                          | Option prices, strikes, expiries, implied volatility, volume, open interest |
| Rates / zero curves             | OptionMetrics / Datastream / treasury-rate data | Discounting and option pricing inputs                                       |
| Dividends                       | OptionMetrics / CRSP / Compustat                | Forward price adjustment and option pricing inputs                          |
| Index membership                | FTSE Russell / CRSP                             | Benchmark context and universe filtering                                    |
| Event-study data                | Eventus                                         | Optional event-study extension                                              |
| News, filings, transcripts      | Factiva / Nexis / S&P Capital IQ Transcripts    | Optional later extension                                                    |

The university access list explicitly includes CRSP, OptionMetrics IvyDB US, Compustat, I/B/E/S, FTSE Russell, Eventus, Datastream, Factiva, and S&P Capital IQ resources.    

---

### 9.2 Minimum Data Required for Version 1

The minimum serious empirical version requires:

```text
CRSP
OptionMetrics IvyDB US
```

This enables:

```text
equity returns
realized volatility
liquidity screens
option-chain cleaning
implied-volatility validation
simple surface construction
volatility forecasting
basic equity/options comparison
```

---

### 9.3 Data Added Later

After the first CRSP and OptionMetrics version works, add:

```text
Compustat
I/B/E/S
```

This enables:

```text
value signals
quality signals
profitability signals
leverage signals
analyst revision signals
forecast dispersion signals
richer equity-only baseline
```

Optional later datasets:

```text
FTSE Russell
Eventus
S&P Capital IQ Transcripts
Factiva / Nexis
Datastream
```

---

### 9.4 Data Licensing Rule

Raw WRDS, CRSP, Compustat, I/B/E/S, and OptionMetrics data will not be published in the public GitHub repository.

The public repository may include:

```text
code
schemas
query templates
data dictionaries
synthetic sample data
small fake option chains
generated figures
methodology
research report
```

The public repository will not include:

```text
raw licensed data
full proprietary option chains
raw CRSP extracts
raw Compustat extracts
raw I/B/E/S extracts
raw OptionMetrics extracts
```

---

## 10. Initial Universe Definition

### 10.1 Base Universe

The base universe will consist of:

```text
US listed optionable equities
common shares only
NYSE / AMEX / NASDAQ listings
sufficient CRSP price history
sufficient OptionMetrics option-chain coverage
minimum stock liquidity
minimum option liquidity
```

---

### 10.2 Suggested First Empirical Universe

The first empirical universe will be:

```text
Top 500 to 1000 US stocks by rolling dollar volume among stocks with usable OptionMetrics option chains
```

This is preferred over “all stocks” because option-chain data is sparse, noisy, and liquidity-dependent.

---

### 10.3 Equity Filters

Initial equity filters:

```text
common shares only
valid CRSP identifier
valid trading date
price greater than $5
minimum 252 trading days of return history
positive rolling dollar volume
top liquidity universe by rolling ADV
exclude obvious stale-price observations
include delisting returns where applicable
```

---

### 10.4 Option Filters

Initial option-chain filters:

```text
valid underlying link
valid option type
valid expiration date
positive time to expiry
non-missing strike
non-missing bid and ask
bid >= 0
ask >= bid
positive midpoint
minimum option open interest or volume
exclude extreme implied-volatility observations
exclude options with too few days to expiry
exclude options with excessive time to expiry for baseline tests
keep liquid OTM calls and puts for simple surface construction
require minimum number of valid strikes per maturity
```

---

### 10.5 Initial Maturity Buckets

Initial maturity buckets:

```text
approximately 30 days
approximately 60 days
approximately 91 days
```

These may later be expanded.

---

## 11. Data Engineering Principles

The data pipeline must enforce:

```text
point-in-time alignment
security identifier mapping
date alignment
data availability dates
signal availability dates
portfolio formation dates
execution dates
return realization dates
survivorship-bias control
lookahead-bias prevention
data-quality auditing
reproducibility
```

The key timing rule is:

```text
signal_date < portfolio_formation_date < execution_date < return_realization_date
```

No same-close execution assumption should be used unless explicitly labelled as a non-tradable diagnostic.

---

## 12. Mathematical Finance Engine

The mathematical finance layer will be built before the full empirical research layer.

### 12.1 Stochastic Process Module

Path simulators to implement:

```text
Brownian motion
Geometric Brownian motion
Ornstein-Uhlenbeck process
simple jump diffusion
```

Concepts covered:

```text
Wiener process
drift
diffusion
Euler-Maruyama discretization
Monte Carlo simulation
mean reversion
jump risk
model misspecification
```

Required tests:

```text
GBM log returns have approximately correct mean and variance
Brownian increments are approximately independent
OU process mean-reverts
jump diffusion produces heavier tails than GBM
```

---

### 12.2 Option Pricing Module

Pricing methods to implement:

```text
Black-Scholes European call and put pricing
binomial tree pricing
Monte Carlo European option pricing
```

Concepts covered:

```text
risk-neutral pricing
replication
no-arbitrage
put-call parity
discounting
terminal payoff
Monte Carlo error
```

Required tests:

```text
put-call parity holds
binomial European prices converge to Black-Scholes prices
Monte Carlo prices converge as number of paths increases
finite-difference Greeks match analytic Greeks
```

---

### 12.3 Greeks Module

Greeks to implement:

```text
delta
gamma
vega
theta
rho
```

Uses:

```text
risk measurement
delta hedging
hedging-error simulations
option-chain diagnostics
surface-aware risk interpretation
```

---

### 12.4 Delta-Hedging Module

The hedging module will simulate the P&L of discretely delta-hedged option positions.

Experiments:

```text
GBM world with correct volatility and no transaction costs
GBM world with incorrect volatility
simple jump world hedged with Black-Scholes delta
discrete hedging with transaction costs
different rebalancing frequencies
```

Outputs:

```text
hedging P&L distribution
mean hedging error
variance of hedging error
tail hedging losses
effect of rebalancing frequency
effect of wrong volatility
effect of jumps
effect of transaction costs
```

Research purpose:

```text
understand the difference between pricing an option and managing the risk of an option position
```

---

## 13. Option Surface Engine

### 13.1 Implied Volatility Solver

The implied-volatility solver will take:

```text
option price
spot price
strike
time to expiry
risk-free rate
dividend yield
call/put flag
```

and return:

```text
implied volatility
convergence flag
failure reason
```

Methods:

```text
bisection
Newton-Raphson
hybrid Newton-bisection fallback
```

Failure flags:

```text
success
failed_no_arbitrage_bounds
failed_no_convergence
failed_bad_input
failed_low_vega
```

Validation:

```text
compare self-computed implied volatility against OptionMetrics implied volatility where available
analyze errors by moneyness
analyze errors by maturity
analyze errors by liquidity
```

---

### 13.2 Simple Volatility Smile Construction

Smile construction will estimate implied volatility as a function of strike or moneyness for a fixed maturity.

Definitions:

```text
moneyness = K / S
log_moneyness = log(K / F)
```

Initial outputs:

```text
ATM implied volatility
put-call skew
smile slope
smile curvature
smile fit error
```

---

### 13.3 Simple Volatility Surface Construction

The volatility surface will estimate implied volatility as a function of strike or moneyness and maturity.

Surface object:

```text
IV(K, T)
```

Initial methods:

```text
moneyness buckets
maturity buckets
linear interpolation
spline smoothing
```

Advanced method:

```text
SABR calibration
```

For the minimum viable project, SABR is optional rather than required.

Surface outputs:

```text
atm_iv_30d
atm_iv_60d
atm_iv_91d
term_structure_slope
skew_30d
surface_curvature
surface_smoothness_error
surface_coverage_score
```

---

### 13.4 Optional SABR Calibration

If time allows, the optional SABR module will fit simplified SABR parameters to observed option smiles.

Parameters:

```text
alpha: volatility level
rho: return-volatility correlation / skew proxy
nu: vol-of-vol
beta: fixed elasticity parameter
```

Baseline beta choices:

```text
beta = 0.5
beta = 1.0
```

Calibration objective:

```text
minimize squared error between observed implied volatilities and SABR-implied volatilities
```

Calibration methods:

```text
scipy.optimize.least_squares
bounded optimization
multiple initializations
robust loss function where needed
```

Extracted features:

```text
sabr_alpha
sabr_rho
sabr_nu
sabr_fit_error
sabr_parameter_stability
```

Interpretation:

```text
alpha: volatility level
rho: implied asymmetry or leverage-effect proxy
nu: volatility-of-volatility or surface instability
fit error: model misspecification or noisy surface
```

---

## 14. Equity Signal Engine

### 14.1 CRSP-Based Signals

Signals from CRSP:

```text
momentum_12_1
short_term_reversal
realized_vol_21d
realized_vol_63d
realized_skew
realized_kurtosis
dollar_volume
turnover
size
market_beta
liquidity_score
```

---

### 14.2 Compustat-Based Signals

Signals from Compustat:

```text
book_to_market
earnings_yield
gross_profitability
return_on_equity
leverage
asset_growth
quality_composite
```

Compustat signals must be lagged to avoid lookahead bias.

Initial assumption:

```text
fundamental data is available only after a conservative reporting lag
```

---

### 14.3 I/B/E/S-Based Signals

Signals from I/B/E/S:

```text
EPS forecast revision
revenue forecast revision
recommendation revision
forecast dispersion
analyst coverage
earnings surprise proxy
```

I/B/E/S signals must use only information available as of the signal date.

---

### 14.4 Signal Normalization

For each raw signal:

```text
winsorize extreme values
z-score cross-sectionally
rank cross-sectionally
sector-neutralize where appropriate
size-neutralize where appropriate
track missingness
track coverage
track signal turnover
lag correctly
```

---

## 15. Options Signal Engine

### 15.1 Vendor Options Signals

Vendor options signals from OptionMetrics where available:

```text
vendor_atm_iv_30d
vendor_atm_iv_60d
vendor_atm_iv_91d
vendor_skew
option_volume
open_interest
put_call_volume_ratio
```

These are baseline option features.

---

### 15.2 Simple Self-Derived Options Signals

Signals derived using the project’s own IV solver:

```text
my_atm_iv_30d
my_atm_iv_60d
my_atm_iv_91d
my_put_call_skew
my_term_structure_slope
my_volatility_risk_premium
my_option_liquidity_score
```

Volatility risk premium definitions:

```text
VRP_vol = implied_volatility - realized_volatility
VRP_var = implied_variance - realized_variance
```

The variance version is preferred for more advanced tests.

---

## 16. Target Variables

### 16.1 Future Equity Returns

```text
forward_21d_excess_return
forward_63d_excess_return
```

Used for:

```text
cross-sectional equity return prediction
long-short portfolio construction
alpha model evaluation
```

---

### 16.2 Future Realized Volatility

```text
future_realized_vol_21d
future_realized_vol_63d
```

Used for:

```text
volatility forecasting
options-feature validation
risk prediction
```

---

### 16.3 Future Drawdown and Tail Events

```text
future_min_return_21d
future_min_return_63d
future_drawdown_63d
large_negative_return_indicator
```

Used for:

```text
tail-risk prediction
drawdown filtering
risk-control evaluation
```

---

## 17. Strategy Families and Experiments

### 17.1 Experiment A: Stochastic Pricing Validation

Question:

```text
Does the pricing engine behave correctly on synthetic data?
```

Tests:

```text
binomial convergence
put-call parity
Monte Carlo convergence
Greek finite-difference checks
hedging error under GBM
```

Purpose:

```text
prove that the mathematical engine works before applying it to real data
```

---

### 17.2 Experiment B: OptionMetrics IV Validation

Question:

```text
Can the self-built implied-volatility solver reproduce vendor implied volatility?
```

Inputs:

```text
OptionMetrics option prices
underlying price
strike
expiry
risk-free rate
dividend yield
call/put flag
```

Outputs:

```text
my_iv
vendor_iv
iv_error
error by moneyness
error by maturity
error by liquidity
error by option type
```

Purpose:

```text
validate the first-principles implementation on real option data
```

---

### 17.3 Experiment C: Simple Surface Quality

Question:

```text
Can a simple volatility smile/surface be fit reliably enough to extract useful research features?
```

Outputs:

```text
ATM implied volatility
skew
term structure
fit error
coverage
```

Purpose:

```text
test whether simple option features are stable enough to use in empirical research
```

---

### 17.4 Experiment D: Volatility Forecasting

Question:

```text
Do option-surface features predict future realized volatility?
```

Compare:

```text
historical realized volatility baseline
vendor ATM implied volatility
self-derived implied volatility
volatility risk premium
simple skew features
combined model
```

Evaluation:

```text
RMSE
MAE
rank IC
volatility bucket accuracy
high-volatility event detection
out-of-sample performance
```

Purpose:

```text
test the most natural empirical use case for option-implied information
```

---

### 17.5 Experiment E: Equity Return Prediction

Question:

```text
Do option-surface features improve cross-sectional equity return prediction?
```

Compare:

```text
equity-only model
equity + vendor options fields
equity + self-derived IV/skew/VRP
full model
```

Evaluation:

```text
rank IC
quintile spread
decile spread
long-short returns
factor-adjusted returns
out-of-sample performance
```

Purpose:

```text
test whether mathematically derived options features improve systematic equity research
```

---

### 17.6 Experiment F: Tail-Risk Filter

Question:

```text
Can option-implied left-tail features reduce drawdowns without destroying returns?
```

Compare:

```text
base equity strategy
base equity strategy + skew filter
base equity strategy + left-tail proxy
```

Evaluation:

```text
max drawdown
CVaR
worst-month return
left-tail return distribution
return sacrificed
net Sharpe
turnover change
```

Purpose:

```text
test whether option-implied risk measures are useful as risk filters rather than pure alpha signals
```

---

### 17.7 Experiment G: Portfolio Construction

Question:

```text
Does the options-informed model survive realistic risk and cost constraints?
```

Compare:

```text
naive decile portfolio
risk-controlled portfolio
cost-aware portfolio
tail-risk-filtered portfolio
```

Evaluation:

```text
gross return
net return
Sharpe ratio
information ratio
max drawdown
CVaR
turnover
cost drag
factor exposure
sector exposure
capacity proxy
```

Purpose:

```text
move from signal research to implementable portfolio research
```

---

## 18. Model Comparison Framework

### 18.1 Main Models

| Model | Inputs                              | Purpose                                   |
| ----- | ----------------------------------- | ----------------------------------------- |
| M0    | Historical realized volatility only | Volatility forecast baseline              |
| M1    | Equity signals only                 | Equity alpha baseline                     |
| M2    | Equity + vendor options fields      | Test basic options data                   |
| M3    | Equity + self-derived IV/skew/VRP   | Test simple first-principles option layer |
| M4    | Full model with simple risk filter  | Practical implementation model            |

For the minimum viable project, this is enough. SABR and density extraction are optional upgrades rather than required pieces.

---

### 18.2 Initial Model Types

Initial models:

```text
equal-weight composite score
cross-sectional OLS
ridge regression
lasso regression
logistic regression for tail-event prediction
```

Optional later models:

```text
gradient boosting
random forest
```

Deep learning will not be used unless there is a clear reason.

---

### 18.3 Validation Design

The project will use time-aware validation.

Allowed validation methods:

```text
walk-forward validation
rolling training window
expanding training window
out-of-sample test period
regime split testing
```

Not allowed:

```text
random train/test split across dates
tuning on the final test set
using future fundamentals
using same-day close execution unless labelled non-tradable
using today’s identifiers for historical security mapping without point-in-time checks
```

---

## 19. Risk Model

The risk model will decompose stock returns into systematic and residual components.

Model form:

```text
stock return = market + sector + style factors + residual
```

Candidate factors:

```text
market
sector / industry
size
value
momentum
quality
volatility
liquidity
option-implied volatility factor
```

Outputs:

```text
factor exposures
factor returns
specific returns
factor covariance
specific risk
portfolio predicted volatility
factor contribution to risk
specific contribution to risk
```

Purpose:

```text
ensure that apparent alpha is not merely hidden exposure to market beta, sector, size, volatility, liquidity, or other systematic factors
```

---

## 20. Portfolio Construction

### 20.1 Portfolio Objective

The portfolio optimizer will conceptually solve:

```text
maximize expected alpha
minus risk penalty
minus transaction cost penalty
minus tail-risk penalty
```

Mathematical form:

```text
maximize: alphaᵀw - λ wᵀΣw - cost(w - w_prev) - γ tail_risk(w)
```

---

### 20.2 Constraints

Candidate constraints:

```text
dollar neutrality
beta neutrality
sector bounds
max single-name position
max gross exposure
max net exposure
liquidity-scaled position limits
turnover cap
option-data coverage requirement
tail-risk exposure limit
minimum diversification
```

---

### 20.3 Portfolio Variants

Portfolio variants:

```text
P1: naive long-short decile portfolio
P2: risk-neutralized long-short portfolio
P3: cost-aware optimized portfolio
P4: options-informed risk-filtered portfolio
```

Purpose:

```text
show the path from raw signal to implementable portfolio
```

---

## 21. Transaction Cost Model

### 21.1 Base Cost Model

Initial cost model:

```text
cost_i = fixed_bps + spread_bps_i + impact_coeff * volatility_i * sqrt(order_size_i / ADV_i)
```

Where:

```text
fixed_bps = baseline fixed trading cost
spread_bps_i = bid-ask spread proxy
impact_coeff = assumed market-impact coefficient
volatility_i = recent realized volatility
order_size_i = dollar value traded
ADV_i = average daily dollar volume
```

---

### 21.2 Cost Stress Tests

The project will test:

```text
0 bps
5 bps
10 bps
25 bps
2x base cost
5x base cost
```

The purpose is not to claim the exact cost model is correct. The purpose is to test whether results survive plausible cost assumptions.

---

### 21.3 Cost Outputs

Outputs:

```text
gross return
net return
turnover
cost drag
capacity proxy
participation rate
implementation shortfall
```

---

## 22. Backtesting Design

The backtester will be calendar-driven.

Backtest loop:

```text
for each rebalance date:
    define eligible universe
    load only data known as of that date
    compute equity signals
    compute options signals
    generate forecasts
    estimate risk
    optimize portfolio
    simulate trades at next tradable date
    subtract transaction costs
    record returns, holdings, trades, exposures
```

Critical timing rule:

```text
signal_date < portfolio_formation_date < execution_date < return_realization_date
```

Outputs:

```text
holdings
trades
daily returns
monthly returns
turnover
transaction costs
factor exposures
sector exposures
drawdowns
attribution
```

---

## 23. Attribution

The attribution system will decompose performance into:

```text
equity signal contribution
vendor option signal contribution
self-derived IV/skew/VRP contribution
market beta contribution
sector contribution
style factor contribution
volatility exposure contribution
tail-risk filter contribution
transaction cost drag
turnover drag
long book contribution
short book contribution
```

Questions attribution should answer:

```text
Did options data add return?
Did options data reduce drawdown?
Did simple option features matter, or only equity signals?
Was improvement just lower beta?
Was improvement just lower volatility exposure?
Did transaction costs erase the benefit?
Was performance concentrated in one regime?
```

---

## 24. Robustness and Falsification

### 24.1 Data Robustness

Test:

```text
different equity liquidity thresholds
different option open-interest filters
different moneyness windows
different maturity buckets
large-cap only universe
high-option-liquidity universe
excluding earnings periods
excluding low-price stocks
excluding low-volume stocks
```

---

### 24.2 Model Robustness

Test:

```text
vendor IV only
self-derived IV only
equity-only model
options-only model
combined options model
```

---

### 24.3 Time Robustness

Test across:

```text
pre-crisis periods
crisis periods
post-crisis periods
COVID period
high-rate period
low-volatility regimes
high-volatility regimes
```

Exact periods will be determined by data availability and final sample window.

---

### 24.4 Cost Robustness

Test:

```text
zero costs
base costs
2x costs
5x costs
```

---

### 24.5 Placebo Tests

Placebo tests:

```text
shuffle option signals cross-sectionally
lag option signals incorrectly as a negative control
random portfolios with the same turnover
same equity model with fake option features
```

---

### 24.6 Statistical Robustness

Statistical checks:

```text
rolling IC
rank IC stability
bootstrap confidence intervals
Sharpe confidence intervals
multiple-testing log
```

---

## 25. Rejection Criteria

The options-surface layer should be rejected or downgraded if:

```text
it only improves in-sample performance
it fails out of sample
it only works in illiquid option names
it is subsumed by simple realized volatility
it is subsumed by beta, size, sector, or liquidity exposure
it adds turnover without improving net performance
it improves raw return but worsens drawdown materially
it depends on unstable implied-volatility estimation
it fails under alternative option filters
it fails under alternative date ranges
it fails under realistic transaction cost assumptions
it cannot be explained economically
```

A negative result is acceptable if it is well-documented.

The goal is not to force the strategy to work. The goal is to test whether derived option-surface features contain useful information.

---

## 26. Known Limitations

Expected limitations:

```text
OptionMetrics data access and licensing constraints
single-name option data can be sparse and noisy
implied-volatility estimation may be unstable for illiquid names
simple surface construction is sensitive to smoothing
transaction cost model is approximate
shorting costs may be simplified or excluded initially
fundamental data availability assumptions may be conservative but imperfect
earnings dates and event effects may require separate handling
results may be universe-dependent
results may be regime-dependent
simple option features may not beat vendor fields
```

These limitations should be reported explicitly rather than hidden.

---

## 27. Minimum Viable Version

The minimum impressive version of the project includes:

```text
1. Black-Scholes pricing
2. binomial tree pricing
3. Greeks
4. GBM simulation
5. one simple additional process such as jump diffusion
6. delta-hedging error simulation
7. implied-volatility solver
8. OptionMetrics IV validation
9. simple volatility smile/surface construction
10. vendor vs self-derived IV/skew comparison
11. volatility forecasting test
12. equity-only vs equity + options model
13. final research report
```

SABR and Breeden-Litzenberger are optional upgrades, not required for the minimum version.

---

## 28. Full Target Version

The full target version includes:

```text
stochastic process simulation
Black-Scholes pricing
binomial pricing
Monte Carlo pricing
Greeks
delta hedging error
implied-volatility solver
option-chain cleaning
simple volatility smile construction
simple volatility surface construction
optional SABR calibration
optional density extraction
equity signals
vendor option signals
self-derived option signals
volatility forecasting
cross-sectional equity return prediction
tail-risk filtering
risk model
portfolio optimizer
transaction cost model
backtesting engine
attribution
robustness suite
final research report
```

---

## 29. Exceptional Version

The exceptional version adds:

```text
SABR calibration across many stock-date-maturity observations
risk-neutral density extraction with quality flags
implied skewness and kurtosis features
left-tail probability features
Markov volatility-regime model
cost-aware portfolio optimization
factor risk attribution
capacity analysis
rejected-strategies appendix
professional documentation
interview summary
```

---

## 30. Deliverables

Final deliverables:

```text
research_charter.md
README.md
theory_notes.md
limitations.md
data_dictionary.md
math_reference.md
synthetic sample data
source code package
unit tests
notebooks
figures
tables
final_research_report.pdf
interview_summary.md
```

---

## 31. First Build Milestone

The first build milestone is not to download WRDS data.

The first build milestone is:

```text
create repository
create synthetic option chain
implement Black-Scholes call and put pricing
implement binomial tree pricing
show binomial convergence to Black-Scholes
add put-call parity test
write first README draft
```

This gives the project a working mathematical foundation before real data is introduced.

---

## 32. First Ten-Week Roadmap

### Week 1: Pricing Skeleton

```text
repo setup
synthetic option chain
Black-Scholes implementation
binomial tree implementation
put-call parity tests
binomial convergence plot
```

---

### Week 2: Stochastic Simulation and Greeks

```text
GBM simulation
Monte Carlo option pricing
analytic Greeks
finite-difference Greeks
basic tests
```

---

### Week 3: Hedging Error

```text
delta-hedging simulator
GBM hedging experiment
wrong-volatility experiment
jump-risk experiment
transaction-cost experiment
```

---

### Week 4: Implied Volatility Solver

```text
bisection solver
Newton-Raphson solver
hybrid fallback
synthetic IV tests
failure flags
```

---

### Week 5: OptionMetrics Small Extract

```text
load small OptionMetrics sample
clean option chains
compute self-derived IV
compare against vendor IV
produce IV validation report
```

---

### Week 6: Volatility Smile and Surface

```text
construct smiles by maturity
construct simple surfaces
compute ATM IV, skew, term structure
produce surface diagnostics
```

---

### Week 7: Optional SABR Calibration

```text
implement SABR calibration
fit selected liquid names
analyze alpha/rho/nu
track fit error and stability
```

---

### Week 8: Simple Tail-Risk Features

```text
construct left-tail proxy
construct skew proxy
construct simple downside-risk features
validate against future drawdowns
```

---

### Week 9: Empirical Signal Tests

```text
build CRSP return panel
construct realized volatility
construct basic equity signals
merge option-surface signals
run volatility forecasting tests
run equity signal comparison
```

---

### Week 10: Backtest and Report

```text
equity-only baseline
equity + vendor options baseline
equity + self-derived options model
basic transaction costs
basic attribution
robustness summary
final report draft
```

---

## 33. Final Research Comparison

The final empirical comparison is:

```text
Equity-only model
vs
Equity + vendor options fields
vs
Equity + self-derived IV/skew/VRP
```

This comparison preserves the systematic equity research project while adding the mathematical finance depth required for options and market-making relevance.

---

## 34. Success Criteria

The project is successful if it can answer, with evidence:

```text
whether self-derived implied volatility roughly matches vendor implied volatility
whether simple option-surface features forecast future realized volatility
whether simple option-surface features improve equity return prediction
whether tail-risk features reduce drawdowns
whether self-derived features beat simple vendor options fields
whether results survive liquidity filters
whether results survive transaction costs
whether results survive out-of-sample validation
whether the mathematical models are stable enough to be useful
```

The project does not require a profitable strategy to be successful.

A mature negative result is acceptable.

---

## 35. Expected Interview Explanation

### 30-Second Explanation

```text
I built a small volatility-surface research platform that connects mathematical finance with systematic equity research. First, I implemented stochastic process simulators, option pricers, Greeks, implied-volatility solvers, and simple volatility-surface tools from first principles. Then I applied those tools to real option-chain and equity data to test whether derived option-implied features improve volatility forecasting, cross-sectional equity selection, tail-risk control, and portfolio construction.
```

---

### 2-Minute Explanation

```text
The project has two layers. The first is a mathematical finance layer, where I build the option-pricing and volatility tools myself: Black-Scholes, binomial trees, Monte Carlo pricing, Greeks, delta-hedging simulations, implied-volatility inversion, and simple volatility-surface construction. The second layer is an empirical research platform using CRSP, OptionMetrics, Compustat, and I/B/E/S data. I compare equity-only models against models that use vendor options fields and models that use my own surface-derived features. The main question is whether mathematically derived option-implied risk measures add useful information for volatility forecasting, equity selection, drawdown control, and portfolio construction after controlling for liquidity, transaction costs, factor risk, and out-of-sample validation.
```

---

## 36. Final Positioning

This project is designed to signal four abilities at once:

```text
1. Mathematical finance ability:
   I can implement stochastic and option-pricing models from first principles.

2. Empirical research ability:
   I can test hypotheses using real financial data without lookahead or survivorship bias.

3. Portfolio/risk ability:
   I understand risk models, transaction costs, attribution, and implementation constraints.

4. Software engineering ability:
   I can build a modular, tested, reproducible research codebase.
```

The project is not simply:

```text
an equity backtest plus an option pricer
```

It is:

```text
a system for deriving option-implied beliefs from market prices and testing whether those beliefs matter in real empirical research
```

That is the central identity of the project.

```

---

If you want, I can next turn this into a **clean `project_outline.md`** right after it, so you have the outline and the charter side by side in matching format.
```
