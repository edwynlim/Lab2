def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average = calc_average(num_list)
    minmax = find_min_max(num_list)
    print(average)
    print(minmax)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input1():
    list = input().split(",")
    for i in range(0, len(list)):
            list[i] = float(list[i])
    print(i)
    print(list)
def get_user_input():
    user_input = input()
    num_list = list()
    input_list = user_input.split(",")
    for items in input_list:
        num_list.append(float(items))
    return (num_list)


def calc_average(num_list):
    # print("calc_average")
    total = 0
    for items in num_list:
        total += items
    average = total / len(num_list)
    return average


def find_min_max(num_list):
    min = max = num_list[0]
    for items in num_list:
        min = min if (min < items) else items
        max = max if (max > items) else items
    return [min, max]

if __name__=="__main__":
    main()

