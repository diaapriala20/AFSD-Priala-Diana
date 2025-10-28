if __name__ == '__main__':
    import string

elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note = [9, 7, 10, 4, 8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

for i in range(len(elevi)):
    nume_elev=elevi[i]
    note_elev=note[i]
    print(nume_elev + "are nota" +str(nota_elev))

