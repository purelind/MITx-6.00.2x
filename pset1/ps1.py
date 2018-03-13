###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #: {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
    import operator
    sorted_cows = sorted(cows.items(), key=operator.itemgetter(1), reverse=True)

    alreay_triped = set()
    result = []

    while len(alreay_triped) < len(sorted_cows):
        trip_res = []
        trip_weight = 0
        for i in range(len(sorted_cows)):
            name, weight = sorted_cows[i][0], sorted_cows[i][1]
            if name not in alreay_triped:
                if trip_weight + weight <= limit:
                    alreay_triped.add(name)
                    trip_res.append(name)
                    trip_weight += weight
        if trip_res:
            result.append(trip_res)

    return result


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #: {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
    # for plan in get_partitions(cows.items()):
    sorted_plan_list = sorted([plan for plan in get_partitions(cows.items())], key=len)

    for plan in sorted_plan_list:
        all_is_well = True
        for trip_plan in plan:
            total_weight = 0
            trip_ok = True

            #: single trip whether overweight.
            for name, weight in trip_plan:
                if total_weight + weight <= limit:
                    total_weight += weight
                else:
                    trip_ok = False
                    break
            if not trip_ok:
                all_is_well = False
                break
            else:
                continue
        if all_is_well:
            return plan
        else:
            continue


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = {'Boo': 20, 'Milkshake': 40, 'MooMoo': 50, 'Miss Bella': 25, 'Lotus': 40, 'Horns': 25}
    start_greedy = time.time()
    greedy_cow_transport(cows, 100)
    end_greedy = time.time()

    start_brute = time.time()
    brute_force_cow_transport(cows, 100)
    end_brute = time.time()

    res = (end_brute-start_brute) > (end_greedy-start_greedy)
    print("greedy faster then brute: %s" % res)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

# cows = load_cows("ps1_cow_data.txt")
# limit=100
# print(cows)
#
# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))


if __name__ == '__main__':
    # cows = {'Boo': 20, 'Milkshake': 40, 'MooMoo': 50, 'Miss Bella': 25, 'Lotus': 40, 'Horns': 25}
    # print(brute_force_cow_transport(cows, 100))
    compare_cow_transport_algorithms()
