'''
Ibrahim Hudson
Comp 163 - 001
2/24/2024
Using PetStore 4 to facilitate a sale
'''

# Outputting Starting Menu
def petStoreMenu():
    print('Welcome to the Aggie Pet Store')
    print('Menu: ')
    print(f'A) Setup Store\nB) Display Pets\nC) Sale Pet\nD) Total Sale\nE) Exit')
petStoreMenu()

# Creating all starter variables
inventory = {
    'Canine': {},
    'Feline': {},
    'Reptile': {}
             }
amount_pet = []
amo_pur = []
cate_choice = []
purchase = {}
transaction_numbers = []
state_tax = 0.07
federal_tax = 0.10
total = 0

# Creating function to create an inventory
def setupStore():
    for i in inventory:
        x = 0
        AmountPet = int(input(f'How many {i} would you like to enter: '))
        amount_pet.append(AmountPet)
        while AmountPet > 0:
            type = input(f'What is the type of {i}: ')
            price = float(input(f'What is the price per {type}: '))
            inventory[i].update({type: price})
            AmountPet -= 1

# Display inventory
def displayinventorypet(inventory):
    print(f'We offer the following pets')
    x = 1
    for i in inventory:
        print(f'{i} :')
        x += 1
        for k in inventory[i]:
            print(f'\t{k} at a cost of ${inventory[i][k]:.2f}.')

# Generate a sale
def sale_pet(category_pet, total):
    if category_pet == '1':
        category_pet = 'Canine'
    elif category_pet == '2':
        category_pet = 'Feline'
    elif category_pet == '3':
        category_pet = 'Reptile'

    cate_choice.append(category_pet)
    print(f'\n{category_pet}'.rjust(20))
    for i in inventory:
        if category_pet == i:
            x = 1
            for k in inventory[i]:
                print(f'\t{x}) {k} at a cost of ${inventory[i][k]:.2f}.')
            type = int(input(f'Enter the type of {category_pet} for purchase: '))
            for k in inventory[i]:
                for k in inventory[i]:
                    keys = []
                    keys.append(k)
                if (type - 1) == keys.index(k):
                    amount_purchase = int(input('Enter the amount for purchase: '))
                    amo_pur.append(amount_purchase)
                    while amount_purchase != 0:
                        total += inventory[i][k]
                        purchase[k] = inventory[i][k]
                        transaction_numbers.append(1)
                        amount_purchase -= 1
                else:
                    continue

        else:
            continue


# Getting info on total sale
def displayReceipt(purchase, total):
    count = 0
    count2 = 0
    x = 0
    purchase2 = []
    for i in purchase:
        purchase2.append(amo_pur[count -1] * purchase[i])
        count += 1
    for i in purchase:
        count2 += 1
        print('aggie pet store bill of sale\n')
        print('_' * 50)
        print(f'{count2}. {cate_choice[x]} {i} ${purchase[i]:.2f} {int(amo_pur[x]):>10} ${purchase[i] * amo_pur[count2 - 1]:.2f}')
        total += purchase[i] * amo_pur[x]
        x += 1
    calculateTax(state_tax, federal_tax, total)
    print(f'\t\tState Tax ${state_tax:.2f}')
    print(f'\t\tFederal Tax ${federal_tax:.2f}')
    print(f'\t\tTotal Due ${total:.2f}')
    print('_' * 50)

# Closing Sale
def closePetStore():
    print('Thank you for using Aggie PetStore\nAggie Pride')

def point_of_sale(purchase, inventory):
    pass

# Calculating tax
def calculateTax(tax1, tax2, total):
    for i in purchase:
        total += purchase[i]
    tax_add = total * tax1
    tax_add2 = total * tax2
    total = total + tax_add + tax_add2
    return total

# Running full program for each available menu choice
def menu_choice(choice):
    if (choice == 'A') or (choice == 'a'):
        setupStore()
        return menu_choice(input('Menu Selection: '))
    elif (choice == 'B') or (choice == 'b'):
        displayinventorypet(inventory)
        return menu_choice(input('Menu Selection: '))
    elif (choice == 'C') or (choice == 'c'):
        x = 1
        for i in inventory:
            print(f'{x}) {i}')
            x += 1
        sale_pet(input('Enter category of pet for sale: '), total)
        return menu_choice(input('Menu Selection: '))
    elif (choice == 'D') or (choice == 'd'):
        print(displayReceipt(purchase, total))
        return menu_choice(input('Menu Selection: '))
    else:
        closePetStore()
# Calling function to start program
menu_choice(input('Enter a Menu Choice: '))