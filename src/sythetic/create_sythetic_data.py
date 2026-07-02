import csv 
import numpy as np 

#How the volume of the stock persists day by day 
persistance_parameter = 0.75
# How violent the daily volume spikes are, 0.25 means it can swing within +- 0.25 to +- 0.5
volume_volatility = 0.25

class Stock():
    def __init__(self, name: str, *, volatilty: float , growth: float, years: int = 2, starting_price: float = 100, cap_profile: str = "medium_cap"):
        self.valid_cap = ["pennystock", "small_cap", "medium_cap", "large_cap", "mega_cap"]
        if cap_profile not in self.valid_cap:
            raise ValueError(
                f"size must be one of {self.valid_cap} got {cap_profile!r}"
            )
        self.name = name
        self.volatilty = volatilty
        self.growth = growth
        self.years = years
        self.starting_price = starting_price
        self.cap_profile = cap_profile
        self.days = 252 * years
        self.prices = None
        self.log_prices_arr = None
        self.log_returns_arr = None
        self.log_vol = None
        self.shares_outstanding_val = None
        self.rng = np.random.default_rng(42)

    def generate_prices(self):
        # Uses GBM to generate the stock prices over the set amount of years 
        
        
        norm = self.rng.normal(0, 1, self.days)
        dt = 1/252

        prices = np.empty(self.days)
        prices[0] = self.starting_price


        for i in range(1,self.days,1):

            #Uses GBM to find the prices
            exponential_factor = (self.growth - 1/2 * self.volatilty** 2 )* dt + self.volatilty * norm[i] *np.sqrt(dt)
            prices[i] = prices [i - 1] * np.exp(exponential_factor)

        self.prices = prices 
        return prices

    def log_prices(self):
        if self.prices is None:
            self.generate_prices()
        #We use the log of the prices so that it is easier to find the daily returns 
        log_prices_arr = np.log(self.prices)
        self.log_prices_arr = log_prices_arr
        return log_prices_arr

    def log_returns(self):
        if self.prices is None:
            self.generate_prices()
        if self.log_prices_arr is None:
            self.log_prices()

        log_returns_arr[0] = 0

        self.log_returns_arr = np.diff(self.log_prices_arr, prepend=self.log_prices_arr[0])

        return log_returns_arr

    def log_volume(self):
        # We take the log volume because the raw volume cannot be negative 

        if self.prices is None:
            self.generate_prices()
        # monetary value of the daily volume 
        
        volume_USD_dict = {
            f"{self.valid_cap[0]}": 500000, #pennystocks
            f"{self.valid_cap[1]}": 10000000, #small cap
            f"{self.valid_cap[2]}":50000000, #mid cap
            f"{self.valid_cap[3]}": 250000000, #large cap
            f"{self.valid_cap[4]}":1000000000  # mega cap
        }  

        volume_USD = volume_USD_dict[self.cap_profile]

        log_mean_vol = np.log( volume_USD/self.prices[0])

        log_vol = np.empty(self.days)
        log_vol[0] = log_mean_vol

        for i in range(1,self.days):
            log_vol[i] = log_mean_vol + persistance_parameter* (log_vol[i - 1] - log_mean_vol) +   self.rng.normal() * volume_volatility

        self.log_vol = log_vol
        return log_vol

    def shares_outstanding(self):
        market_cap_USD={
            f"{self.valid_cap[0]}": 250_000_000, #pennystocks
            f"{self.valid_cap[1]}": 1_000_000_000, #small cap
            f"{self.valid_cap[2]}":5_000_000_000, #mid cap
            f"{self.valid_cap[3]}": 100_000_000_000, #large cap
            f"{self.valid_cap[4]}":500_000_000_000  # mega cap
        }


        self.shares_outstanding_val = market_cap_USD[self.cap_profile]/self.prices[0]
        return self.shares_outstanding_val

        


