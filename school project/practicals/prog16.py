def print_stick(n):
    print("o " * n)
    print(" " * n)
    print("| " * n)

total_stick = 21
win = False
human_player = True

print("==== Welcome To Stick Picking Game :: Computer Vs User ====")
print("Rule: 1) Both User and Computer can pick sticks between 1 to 4 at a time")
print(" 2) Whosoever picks the last stick will be the loser")
print(" Let's Begin ==")
player_name = input("Enter Your Name: ")

print_stick(total_stick)

while not win:
    if human_player:
        print("You Can Pick sticks between 1 to 4")
        user_pick = 0
        while user_pick <= 0 or user_pick > 4:
            user_pick = int(input(player_name + ": Enter Number of Sticks to Pick: "))
        total_stick -= user_pick
        human_player = False
        print_stick(total_stick)
        print("*" * 60)
        input("Press Enter to continue...")
    else:
        computer_pick = 5 - user_pick
        print("Computer Picks:", computer_pick, "Sticks")
        total_stick -= computer_pick
        print_stick(total_stick)
        if total_stick == 1:
            print("## WINNER: COMPUTER ##")
            win = True
            print("*" * 60)
            input("Press Enter to continue...")
            break
        human_player = True
