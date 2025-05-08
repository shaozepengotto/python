#怎样处理用户输入的数字？例如，我想让用户输入 cracker 和 cheese 的数量，该怎么办？记住，使用 int()把 input()的值转换为整数。
def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {box_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

print("how many cheeses do you have?")
cheese_count = int(input())

print("How many boxes of crackers do you have?")
box_of_crackers = int(input())

