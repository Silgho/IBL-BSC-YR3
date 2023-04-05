"""This is a programme which replaces each white space with ... (i.e three periods)"""
def playback_replacer():
    user_name = input("To continue, Please enter your name : ")
    print("Hello " +user_name+ " , Welcome to playback. ")
    user_input = input("Enter your task  : ")

    play_back = user_input.replace(" ", "...")

    print("Problem solved and the solution is : ")
    print(play_back)


playback_replacer()