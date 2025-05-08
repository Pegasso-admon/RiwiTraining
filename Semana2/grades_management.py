# Grades management system
""" 
El programa debe:

1    Determinar el estado de aprobación:
        Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
        Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
2    Calcular el promedio:
        Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
        Calcular y mostrar el promedio de las calificaciones en la lista
3    Contar calificaciones mayores:
        Preguntar al usuario por un valor específico
        Contar cuántas calificaciones en la lista son mayores que este valor
4    Verificar y contar calificaciones específicas:
        Preguntar al usuario por una calificación específica. 
        Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa. 
"""

Grades = [] #Over here Im creating an empty list where the program is saving the grades that the user is adding 
Flag = True

while Flag: #I will start the loop to show the menu
    print("""\n---------------- Calificaciones Menu ---------------\n 
          1. Enter a grade to see if you approved or failed.
          2. Please enter a list of grades.
          3. Calculate the GPA.
          4. Count grades greater than one value.
          5. Verify and count specific grade.
          6. Exit system.
 """)
    
    try:
        options = int(input("Please enter a number between 1 and 6: "))
    except ValueError: 
        print("Please enter a valid number, remember that it must be between 1 and 6.")
        continue #Then I will proceed with this validation for the menu

    match options:
        case 1: 
            #For the option number 1, the system will ask the user for a single grade to add to the list that I defined some code lines before
            try: 
                grade = int(input("Please enter a grade(Remember that it must be a number between 0 and 100): "))
                if 0 <= grade <= 100: 
                    Grades.append(grade)
                    if grade >= 70: 
                        print("You approved!")
                    else: 
                        print("You failed :(")
                else: 
                    print("The grade must be between 0 and 100, try again!")
            except ValueError:
                print("Please enter a valid number.")

        case 2:
            #For the option number 2, the system will ask the user for several grades that will be storaged in the empty list
            calculation = input("Please enter the grades separated by commas(like this: 100,90,80): ")
            for g in calculation.split(','):
                g = g.strip()
                if g.isdigit(): 
                    num = int(g)
                    if 0 <= num <= 100:
                        Grades.append(num)
            print("Updated list:", Grades)

        case 3: 
            #For the option number 3, the system will give the user the GPA (Grade point average)
            if Grades:
                total = 0 
                for g in Grades:
                    total += g 
                print(f"GPA: {total / len(Grades):.2f}")
            else: 
                print("The list is empty.")
        
        case 4: 
            #For the option number 4, the system compares all stored grades to a reference value enter by the user.
            try:
                ref = int(input("Compare with which value?: "))
                count = 0
                i = 0
                while i < len(Grades):
                    if Grades[i] > ref:
                        count += 1
                    i += 1
                print(f"{count} Grades are higher than {ref}.")
            except ValueError:
                print("Invalid, try again!")

        case 5: 
            #For the option number 5, the system will verify and compare the grade that the user entered in the list and it will say how many times appears 
            target = int(input("Which grade are you looking for?: "))
            count = 0
            found = False
            for g in Grades:
                if g != target:
                    continue  
            found = True
            count += 1
            if found:
                print(f"The grade {target} appears {count} times.")
            else:
                print(f"The grade {target} is not in the list.")

        case 6: 
            #For the option number 6 the user can exit the system.
            print("Thanks for using the system ;D!")
            Flag = False

        case _: 
            #I use this when the user enter a number that is not in the range of 1 and 6
            print("Invalid option, try again!")





