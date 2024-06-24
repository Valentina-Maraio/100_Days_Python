line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

treasure_map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input()

# Where do you want to put the treasure?

if position == 'A1':
    line1[0] = 'X'
elif position == 'B1':
    line1[1] = 'X'
elif position == 'C1':
    line1[-1] = 'X'
elif position == 'A2':
    line2[0] = 'X'
elif position == 'B2':
    line2[1] = 'X'
elif position == 'C2':
    line2[-1] = 'X'
elif position == 'A3':
    line3[0] = 'X'
elif position == 'B3':
    line3[1] = 'X'
else:
    line3[-1] = 'X'
print(f"{line1}\n{line2}\n{line3}")

'''
Their solution: 
    trasforma l'input in minuscoolo
    letters = position[0].lower()
    sappiamo che le tre colonne sono a, b, c
    quindi ha senso scrivere abc come una lista di lettere
    abc = ['a', 'b', 'c']
    automaticamente la lista ha degli indici
    a1, b1, c1
    a2, b2, c2
    a3, b3, c3
    per sapere l'indice non devo leggerlo dall'input
    mi basterá sapere la lettera e automaticamente sapró l'indice corrispondente
    letter_index = int(position[1]) - 1
    qui sto mettendo la X nell'indice indicato nell'input
    map[number_index][letter_index] = 'X'
'''
