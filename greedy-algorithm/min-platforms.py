"""

Implement a function that returns the minimum number of platforms that are required for the train so that none of them waits.

Input#
Two lists which represent arrival and departure times of trains that stop

Output#
Minimum number of platforms required

The time complexity will now be O(nlogn)
, because we used sorted lists and greedily kept track of the trains that have arrived but haven’t left yet.

"""
def find_platform(arrival, departure):
    n = len(arrival)
    arrival.sort()
    departure.sort()
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    # Similar to merge in merge sort to process all events in sorted order
    while i < n and j < n:
        # If next event in sorted order is arrival, increment count of platforms needed
        if arrival[i] < departure[j]:
            plat_needed += 1
            i += 1
            if plat_needed > result:
                result = plat_needed
        else:
            plat_needed -= 1
            j += 1
    return result


# Driver code to test above function
if __name__ == '__main__':

    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]

    print(find_platform(arrival, departure))

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 240, 320, 430, 400, 520]

    print(find_platform(arrival, departure))
