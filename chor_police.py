import random

S = int(input("Number of time u want to play : "))
i = 1

while i <= S:

    msg = "Welcome to Thief-Police game"
    msg1 = "Police: Hello everyone, I will catch the thief with index no"
    print(msg)
    nums = [00, 80, 60, 100]
    random.shuffle(nums)
    print(nums)
    mylist = [n for n in nums]

    x = int(input('choose a card from (0-3). '))

    player1 = mylist[x]
    mylist.remove(mylist[x])
    player2 = mylist[0]
    player3 = mylist[1]
    player4 = mylist[2]

    print('Player 1 is', player1)
    print('Player 2 is', player2)
    print('Player 3 is', player3)
    print('Player 4 is', player4)

    new_list = [n for n in mylist]
    print(new_list)

    def find_babu():
        if player2 == 100:
            print("Player 2: I'm the boss with index no", nums.index(100))

        elif player3 == 100:
            print("Player 3: I'm the boss with index no", nums.index(100))

        elif player4 == 100:
            print("Player 4: I'm the boss with index no", nums.index(100))


    def find_dakat():
        if player2 == 60:
            print("Player 2: I'm the Robber")

        elif player3 == 60:
            print("Player 3: I'm the Robber")

        elif player4 == 60:
            print("Player 4: I'm the Robber")


    def find_police():

        if player2 == 80:
            print("Player 2: I'm the police with index no", nums.index(80))

        elif player3 == 80:
            print("Player 3: I'm the police with index no", nums.index(80))

        elif player4 == 80:
            print("Player 4: I'm the police with index no", nums.index(80))


    def find_thief():
        y = int(input('Choose the index no of thief excluding index no of boss and thief from (0-3). '))
        local_thief = nums

        if (y == local_thief.index(00)):
            print('You are correct')
        else:
            print('You are not correct')


    def call_police():

        local = nums
        local.remove(100)
        local.remove(80)
        random.shuffle(local)
        print(local)
        print("Polic: The value of thief - ", local[0])
        if (local[0] == 60):
            print("Police is failure to catch the thief")
        else:
            print("Police have caught the thief")

    if (player1 == 00):
        print(' You have got the "Thief = 00" card ')
        print(msg1 , nums.index(80))
        print(find_babu())
        print(call_police())

    elif (player1 == 80):
        print(' You have got the "Police = 80" card with index no ', nums.index(80))
        print(find_babu())
        print(find_thief())

    elif (player1 == 60):
        print(' You have got the "Robber = 60" card')
        print(msg1, nums.index(80))
        print(find_babu())
        print(call_police())

    elif (player1 == 100):
        print(' Your have got the "Boss = 100" card with index no ', nums.index(100))
        print(msg1, nums.index(80))
        print(call_police())

    i = i+1

