# creating the list of songs
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
#

sum_time = 0.0
songs_amount = int(input("How many songs do you want to choose?\n"))
for t in range(songs_amount):
    name = input(f'Enter the name of № {t + 1} song:')
    for i in range(len(violator_songs)):
        if name == violator_songs[i][0]:
            print(violator_songs[i][1])
            sum_time += violator_songs[i][1]

print("Total time:", sum_time, "min")
