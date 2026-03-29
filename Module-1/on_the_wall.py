# Jeff Victorino
# 03/29/2026
# Module 1.3 Assignment

# prints how many bottles of beers are on the wall from n to 1
def countdown(bottles):
    # Count down from the given number to 1
    while bottles > 0:
        # x bottles remain
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall")
            print(f"{bottles} bottles of beer")
            print("Take one down, pass it around")
            print(f"{bottles-1} bottle(s) of beer on the wall\n")

        # 1 bottle remains
        else:
            print("1 bottle of beer on the wall")
            print("1 bottle of beer")
            print("Take one down, pass it around")
            print("0 bottles of beer on the wall\n")
        
        bottles -= 1


# main function
def main():
    # ask for number of bottles
    bottles = int(input("How many bottles of beer are on the wall? "))
    countdown(bottles)
    print("Time to buy more bottles of beer!")


if __name__ == "__main__":
    main()