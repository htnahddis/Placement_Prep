def find_platform(arrival, departure):
    arrival.sort()
    departure.sort()

    l = 0
    m = 0

    platforms = 0
    max_platforms = 0

    while l < len(arrival) and m < len(departure):

        if arrival[l] <= departure[m]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            l += 1

        else:
            platforms -= 1
            m += 1

    return max_platforms


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(find_platform(arr, dep))