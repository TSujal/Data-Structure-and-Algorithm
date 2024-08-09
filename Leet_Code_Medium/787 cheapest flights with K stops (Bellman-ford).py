"""
Solve by: Sujal Thakkar
Problem  787 Leet-code : cheapest Flight problem with k stops.
"""
"""
There are n cities connected by some number of flights.
You are given an array flights where
flights[i] = { from[i], to[i], price[i] } indicates that there is a flight
from city from[i] to city to[i] with cost price[i].

You are also given three integers src, dst, and k, return
the cheapest price from src to dst with AT MOST K STOPS.
If there is no such route, return -1.
"""
# we will be using Bellman ford algorithm, as because of {AT MOST K STOPS} we cannot use Dijkstra as its inefficient
# O(E.K), number of edges * keys
# and we have k = 1 in here.
#here we are given a source node ie 1 and Destination 2, which we need to mention inside the function
#so we are going to do K + 1, BFS
# and because we do have K, the number of time we will iterate, we also need a TEMP ARRAY to store all the values.
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n #assiging all the values to INF
        prices[src] = 0 #keeping the source price to 0

        #iteration begin which will be K + 1 times.
        for i in range(k+1):
            tempPrices = prices.copy() #its going to copy the price array
            for s,d,price in flights: # s = Source, d = destination
                if prices[s] == float("inf"):
                    continue
                if prices[s] + price < tempPrices[d]:
                    tempPrices[d] = prices[s] + price
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]



if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))
    #should output 500
