def mileage_info():
    def create_mileage_list(epa_file):
        mileage_list = []  # creates line
        epa_file.readline()              # read first lines
        for line in epa_file:            # 2b. get each line from the file
            line_list = line.split(',')  # 2bI. csv => split on comma
            car_tuple = (int(line_list[10]), line_list[2], line_list[3])
            mileage_list.append(car_tuple)  # 2bII . append t u p l e
        return mileage_list

    def find_max_min_mileage(mileage_list, max_mileage, min_mileage):
        max_min_mileage_list = []  # make a list of vehicles within interval
        # finds vehicles between interval
        for car_tuple in mileage_list:
            if max_mileage >= car_tuple[0] >= min_mileage:
                max_min_mileage_list.append(car_tuple)
        return max_min_mileage_list
    # open EPA file
    epa_file = open("epadata2015.csv", "r")
    #  ask user for interval
    mileage_list = create_mileage_list(epa_file)
    print("\nFind the vehicles that are within a certain Hwy mpg interval (2015):")
    max_mileage = int(input('  enter max mpg: '))
    min_mileage = int(input('  enter min mpg: '))
    print()

    max_min_mileage_list = \
        find_max_min_mileage(mileage_list, max_mileage, min_mileage)
    # prints list within interval
    print('Make and models: ')
    for car_tuple in max_min_mileage_list:
        print(" ", car_tuple[1], car_tuple[2])


def trend_plot():
    global title
    import pylab
    import csv

    epa_file = open("epadata2020.csv", "r")
    x, y = [], []
    reader = csv.reader(epa_file)  # reads file
    #  ask user for input
    print('\nEnter "H" for Highway MPG.\nEnter "C" for city MPG\nEnter "O" for OverallMPG.')
    trend_option = input('Please choose one of the above option for the graph: ')
    trend_option = trend_option.upper()
    check = 'HCO'

    # check for mistake input
    while len(trend_option) != 1 or trend_option not in check:
        trend_option = input('"H", "O" or "C" only, please try again: ')
        trend_option = trend_option.upper()
        check = 'HCO'

    if trend_option == "H":
        title = "Highway MPG"
        next(reader)
        for line_list in reader:
            try:
                year_list = int(line_list[0])
                x.append(year_list)
                highway_mpg_float = float(line_list[6])
                y.append(highway_mpg_float)
            except ValueError:
                break
    elif trend_option == "C":
        title = "City MPG"
        next(reader)
        for line_list in reader:
            try:
                year_list = int(line_list[0])
                x.append(year_list)
                highway_mpg_float = float(line_list[5])
                y.append(highway_mpg_float)
            except ValueError:
                break
    elif trend_option == "O":
        title = "OverallMPG"
        next(reader)
        for line_list in reader:
            try:
                year_list = int(line_list[0])
                x.append(year_list)
                highway_mpg_float = float(line_list[4])
                y.append(highway_mpg_float)
            except ValueError:
                break
    # ask user for display or save to file
    print('\nEnter "D" for Display on screen\nEnter "F" to save to File')
    display_file = input('Please choose one of the above option for the graph: ')
    display_file = display_file.upper()
    check = 'DF'
    while len(display_file) != 1 or display_file not in check:
        display_file = input('"D" or "F" only, please try again: ')
        display_file = display_file.upper()
        check = 'ED'

    if display_file == "D":
        print("display")
    elif display_file == "F":
        print("file")

    epa_file.close()

    pylab.plot(x, y)
    pylab.ylabel(title)
    pylab.xlabel("Year")
    pylab.title("EPA annual average highway MPG data")

    if display_file == "D":
        pylab.show()
    elif display_file == "F":
        pylab.savefig("epa_plot.png")


# introduction
print("Welcome to the vehicle fuel consumption app \n")
print(
    "In this app you will find lists of information about fuel economy data that "
    "\nThe US Environment Protection Agency (EPA) published for 2015 and 2020.\n")
# use input option
option = int(input('Enter "1" for list of  2015 EPA data or "2" for graph of the latest EPA data until 2020: '))
if option == 1:
    mileage_info()
elif option == 2:
    trend_plot()
else:
    print('Unknown value, restart to try again.')
