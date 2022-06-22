#!/usr/bin/env python3
# python3 solver_aki.py input_0.csv output_0.csv
# python3 solver_aki.py input_1.csv output_1.csv
# python3 solver_aki.py input_2.csv output_2.csv
# python3 solver_aki.py input_3.csv output_3.csv
# python3 solver_aki.py input_4.csv output_4.csv
# python3 solver_aki.py input_5.csv output_5.csv
# python3 solver_aki.py input_6.csv output_6.csv

import sys
import math
import csv

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)
    global dist
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour

def swap(tour, cities, swapped_or_not):
    N = len(cities)

    for i in range(N-2):
        p_0 = tour[i]
        p_1 = tour[i+1]
        for j in range (i+2, N-1):
            q_0 = tour[j]
            q_1 = tour[j+1]
            if (dist[p_0][p_1] + dist[q_0][q_1]) > (dist[p_1][q_1] + dist[p_0][q_0]):
                swapped_or_not = True
                # swap!
                tour[i+1], tour[j] = tour[j], tour[i+1]
                
    return tour, swapped_or_not



if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    tour = solve(cities)
    # swapping until there's no chance to improve
    swapped_or_not = True
    while swapped_or_not == True:
        swapped_or_not = False
        tour, swapped_or_not = swap(tour, cities, swapped_or_not)
        print("swap!")
    print_tour(tour)
    filename = sys.argv[2]
    with open(filename, mode = 'w') as f:
        writer = csv.writer(f, delimiter='\n')
        # tour_output = ['index' + '\n'.join(map(str, tour))]
        writer.writerow(['index'])
        for i in range(len(tour)):
            writer.writerow([tour[i]])
