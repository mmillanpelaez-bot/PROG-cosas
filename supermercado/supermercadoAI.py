# SUPERMARKET.py
# Interactive menu with pause after showing results

cash_registers = [
    ['1', [100, 1], [50, 13], [20, 5]],
    ['3', [50, 21], [20, 11], [10, 7], [0.02, 4]],
    ['2', [50, 2], [20, 9], [0.50, 12], [0.20, 13]]
]

def calculate_register_amount(register):
    total = 0.0
    for denomination, quantity in register[1:]:
        total += denomination * quantity
    return total

def show_totals_per_register():
    grand_total = 0.0
    for register in cash_registers:
        reg_id = register[0]
        reg_total = calculate_register_amount(register)
        grand_total += reg_total
        print(f"Total in register {reg_id}: {reg_total:.2f} €")
    print("-" * 40)
    print(f"Grand total in all registers: {grand_total:.2f} €")
    pause()

def show_totals_per_denomination():
    denomination_totals = {}
    for register in cash_registers:
        for denomination, quantity in register[1:]:
            if denomination not in denomination_totals:
                denomination_totals[denomination] = 0
            denomination_totals[denomination] += quantity

    print("\nTotals per denomination across all registers:")
    for denomination in sorted(denomination_totals.keys(), reverse=True):
        qty = denomination_totals[denomination]
        subtotal = denomination * qty
        print(f"{qty} x {denomination:.2f} € = {subtotal:.2f} €")
    pause()

def show_single_register_total():
    target_id = input("Enter the register ID: ").strip()
    found = False
    for register in cash_registers:
        if register[0] == target_id:
            total = calculate_register_amount(register)
            print(f"Total in register {target_id}: {total:.2f} €")
            found = True
            break
    if not found:
        print(f"Register with ID '{target_id}' not found.")
    pause()

def pause():
    """Pause until user presses Enter or 0 to return to menu."""
    choice = input("\nPress Enter to continue or 0 to return to the main menu: ")
    # If user presses 0, just return (menu will show again)
    # If user presses Enter, also return (same effect)

def main_menu():
    while True:
        print("\n--- SUPERMARKET MENU ---")
        print("1. Show totals per register")
        print("2. Show totals per denomination")
        print("3. Show both")
        print("4. Show total for a specific register")
        print("5. Exit")
        option = input("Choose an option (1-5): ").strip()

        if option == "1":
            show_totals_per_register()
        elif option == "2":
            show_totals_per_denomination()
        elif option == "3":
            show_totals_per_register()
            show_totals_per_denomination()
        elif option == "4":
            show_single_register_total()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()
