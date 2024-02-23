from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_prices = [10**20] * n
        flights_prices[src] = 0

        for i in range(k + 1):
            # create a temp array, because otherwise it will not consider the number of stop propely
            copy_prices = flights_prices[::]

            # iterate through prices and update each node to its lowest price, that we need to get to it
            for source, dest, price in flights:
                if flights_prices[source] == 10**20:
                    continue
                copy_prices[dest] = min(copy_prices[dest], flights_prices[source] + price)

            # update flights array to the copy, where new values are stored
            flights_prices = copy_prices
        
        # if we cant reach the dst return -1
        if flights_prices[dst] == 10 ** 20:
            return -1
        else:
            return flights_prices[dst]