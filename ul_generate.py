import random


def main():
    generate_ul(10, "ul_10")
    generate_ul(100, "ul_100")
    generate_ul(1000, "ul_1k")
    generate_ul(10000, "ul_10k")
    generate_ul(100000, "ul_100k")
    generate_ul(1000000, "ul_1m")




def generate_ul(x, name):
    unsorted_list = random.sample(range(x+1), x)
    file_name = f"{name}.csv"
    with open(file_name, 'w') as file:
        for number in unsorted_list:
            file.write(f"{number}, ")


if __name__ == "__main__":
    main()