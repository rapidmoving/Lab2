def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    temp_list = get_user_input()
    average = calc_average(temp_list)
    print("Average = ", average)
    find_min_max(temp_list)
def display_main_menu():
    print("Enter some numbers separated by commas (e.g 5, 65, 21)")

def get_user_input():
    number = input("Enter the numbers: ")
    num_list = number.split(",")
    temp_list = []
    temp_list = list(map(float, num_list))
    print(temp_list)
    return temp_list

def calc_average(temp_list):
    total = sum(temp_list)
    average = total/(len(temp_list))
    return average

def find_min_max(temp_list):
    maximum = int(max(temp_list))
    minimum = int(min(temp_list))
    min_max = [minimum, maximum]
    print(min_max)
    return min_max

# def sort_temperature():
#
#
#
# def calc_median_temperature():




if __name__ == "__main__":
    main()
