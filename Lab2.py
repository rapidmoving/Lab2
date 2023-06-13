def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    average = calc_average(temp_list)
    print("Average = ", average)

    min_max=[]
    min_max=find_min_max(temp_list)
    print("Minimum = ", min_max[0],", Maximum = ", min_max[1])

    sorted_list = sort_temperature(temp_list)
    median = calc_median_temperature(sorted_list)
    print("Median = " + str(median))

def display_main_menu():
    print("Enter some numbers separated by commas (e.g 5, 65, 21)")


def get_user_input():
    number = input("Enter the numbers: ")
    num_list = number.split(",")
    temp_list = []
    temp_list = list(map(float, num_list))
    return temp_list


def calc_average(temp_list):
    total = sum(temp_list)
    average = total/(len(temp_list))
    return average


def find_min_max(temp_list):
    maximum = int(max(temp_list))
    minimum = int(min(temp_list))
    min_max = [minimum, maximum]
    return min_max


def sort_temperature(temp_list):
    temp_list.sort()
    print(temp_list)
    return temp_list


def calc_median_temperature(sorted_list):
    midpoint = (len(sorted_list)/2)
    middle = int(midpoint)
    if midpoint % 2 == 0:
        median = (sorted_list[middle] + sorted_list[middle - 1]) / 2
    else:
        median = sorted_list[middle]
    return median



if __name__ == "__main__":
    main()
