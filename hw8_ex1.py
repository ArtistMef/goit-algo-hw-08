import heapq

def minimize_connection_cost(cable_lengths):
    
    total_cost = 0
    heapq.heapify(cable_lengths)
    while len(cable_lengths) > 1:
        first_smallest = heapq.heappop(cable_lengths)
        second_smallest = heapq.heappop(cable_lengths)
        cost = first_smallest + second_smallest
        heapq.heappush(cable_lengths, cost)
        total_cost += cost
    return total_cost

cable_lengths = [5, 4, 2, 8, 3, 11]
min_cost = minimize_connection_cost(cable_lengths)
print(min_cost)
