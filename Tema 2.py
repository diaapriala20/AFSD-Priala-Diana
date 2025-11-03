if __name__ ==" __main__":
    # 1. Declarăm un șir (textul poate fi copiat de pe un site de știri)
    text = """România a înregistrat o creștere semnificativă a turismului intern în acest an.
    Multe persoane au ales să viziteze zone montane și stațiuni de pe litoral."""

    # 2. Împărțim textul în două părți egale
    lungime = len(text)
    jumatate = lungime // 2  # împărțire întreagă
    prima_parte = text[:jumatate]
    a_doua_parte = text[jumatate:]

    # 3. Operații pe prima parte
    prima_parte = prima_parte.upper()  # toate literele majuscule
    prima_parte = prima_parte.strip()  # elimină spațiile de la început și final

    # 4. Operații pe a doua parte
    a_doua_parte = a_doua_parte[::-1]  # inversează ordinea caracterelor
    a_doua_parte = a_doua_parte.capitalize()  # prima literă devine majusculă

    # elimină semnele de punctuație . , ! ?
    for semn in [".", ",", "!", "?"]:
        a_doua_parte = a_doua_parte.replace(semn, "")

    # 5. Combinăm cele două părți
    rezultat = prima_parte + " " + a_doua_parte

    # 6. Afișăm rezultatul final
    print("Rezultatul final este:\n")
    print(rezultat)
