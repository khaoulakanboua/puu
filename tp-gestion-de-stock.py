liste = {} 

while True: 
 
    print("\nSelect a choice")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Item")
    print("4. Exit")
    
    choice = input("Enter your choice : ")
    
    if choice == "1": 
        itemName = input("Enter Item Name : ")
        itemQuantity = int(input("Enter Item Quantity : "))
        unitPrice = float(input("Enter Unit Price : "))
        
        if itemName in liste: 
            liste[itemName]["quantity"] += itemQuantity
            liste[itemName]["unit-Price"] = unitPrice
        else:
             liste[itemName] = {"quantity": itemQuantity, "unit-Price": unitPrice}
            
        print("Item successfully Added !")
        
    elif choice == "2": 
        itemName = input("Enter name of item : ")
        
        if itemName in liste: 
            del liste[itemName]
            print("Item successfully removed !")
        else: 
            print("Item out of stock.")
            
    elif choice == "3":
        total_stock = 0 
        
       
        print("--------------")
        print("\nCurrent stock :")
        print("--------------")
        print("{:<20} {:<10} {:<10} {:<10}".format("Name", "quantity", "Unit Price", "Total Price"))
        
        for itemName, item in liste.items():
            itemQuantity = item["quantity"]
            unitPrice = item["unit-Price"]
            totalPrice = itemQuantity * unitPrice
            
            print("{:<20} {:<10} {:<10} {:<10}".format(itemName, itemQuantity, unitPrice, totalPrice))
            
            total_stock += totalPrice 
            
        print("--------------")
        print("--------------")
        print("Total stock value : {:.2f}".format(total_stock))
        
    elif choice == "4": 
       
        break
    
    else: 
        print("Invalid choice.")
