expenses=[]

  

def show_expenses(month):
    for expense_amount, expense_type,expense_month in expenses:
        if expense_month==month:
            print(f'{expense_amount}-{expense_type}')



def add_expense(month):
    print()
    expense_amount=int(input("Podaj kwotę w [zł]: "))
    expense_type=input("Podaj typ wydatku(jedzenie,rozrywka,dom,inny): ")

    expense=(expense_amount, expense_type, month)
    expenses.append(expense)


def show_stats(month):
    total_amount_this_month =sum(expense_amount for expense_amount,_, expense_month in expenses if expense_month==month)
    number_of_expenses_this_month = sum(1 for _,_, expense_month in expenses if expense_month==month)
    average_expanses_this_month = total_amount_this_month/number_of_expenses_this_month
    total_amount_all =sum(expense_amount for expense_amount,_, _ in expenses)
    average_expanses_all = total_amount_all/ len(expenses)


    print()
    print("Statystyki")
    print("Wszystkie wydatki w tym miesiącu:", total_amount_this_month)
    print("Średnie wydatki w tym miesiącu:", average_expanses_this_month)
    print("Wszystkie wydatki:", total_amount_all)
    print("Średni wydatek:", average_expanses_all)



while True:
    print()
    month=int(input("Wybierz miesiąc[1-12]: "))

    if month==0 or month>12:
        print("Nieprawidłowa wartość!")
        break

    while True:
        print()
        print("0 - Wróc do wyboru miesiąca")
        print("1 - Wyświetl wszystkie wydatki")
        print("2 - Dodaj wydatek")
        print("3 - Statystyki")

        choice=int(input("Wybierz opcje: "))

        if choice==0:
            break

        if choice==1:
            show_expenses(month)
            
        if choice==2:
            add_expense(month)

        if choice==3:
            show_stats(month)