if __name__ ==" __main__"

 elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
 note = [9, 7, 10, 4, 8]

 elev_nou = "Felix"
 nota_elev_nou = 6
 elev_de_sters = "Darius"

 interogari_nume = ["Ana", "Mara", "Elena", "stop"]

 absente = [1, 0, 2, 3, 0]

 for i in range(len(elevi))
     nume_elev=elevi[i]
     note_elev=note[i]
     print(nume_elev + "are nota" +str(nota_elev))

nota_maxima=max
nota_minima=min

print("\nA2. Nota maximă și minimă:")
print("Nota maximă este", nota_maxima, "obținută de:")
for i in range(len(note)):
if note[i] == nota_maxima:
print(" -", elevi[i])

print("Nota minimă este", nota_minima, "obținută de:")
for i in range(len(note)):
if note[i] == nota_minima:
 print(" -", elevi[i])

 media = sum(note) / len(note)
 print("\nA3. Media clasei este:", format(media, ".2f"))

print("\nA4. Elevii promovați (nota >= 5):")
for i in range(len(note)):
if note[i] >= 5:
print(" -", elevi[i])

elevi = ["Ana", "Bogdan", "Cristina", "David", "Elena"]
note = [8, 9, 6, 7, 10]

print(f"Liste inițiale:")
print(f"Elevi: {elevi}")
print(f"Note: {note}\n")

print("### B5. Creșterea Notelor cu 1 (max 10) ###")
for i in range(len(note)):
    if note[i] < 10:
        note[i] += 1

print(f"Note actualizate după B5: {note}\n")

print("### B6. Adăugarea unui Elev Nou ###")
elev_nou = "Mihai"
nota_elev_nou = 9

print(f"Liste după B6:")
print(f"Elevi: {elevi}")
print(f"Note: {note}\n")

print("### B7. Ștergerea unui Elev Predefinit ###")
elev_de_sters = "David"

