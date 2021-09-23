'''
Write a function 'music_func' that takes 3 parameters -- music type, music group, vocalist -- and prints them all out as shown in the example below. In case no input is provided by the user, the function should assume these default values for the parameters: "Classic Rock", "The Beatles", "Freddie Mercury".

The main program is given.

Example input/output:
'''


#definition for music_func goes here

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()