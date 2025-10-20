"""
Simple Calculator - Command Line Interface
Codveda Technology - Python Development Internship
Task: Level 1 - Simple Calculator

This program performs four basic arithmetic operations:
Addition, Subtraction, Multiplication, and Division
"""

def add(x, y):
    """Returns the sum of x and y"""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y"""
    return x - y

def multiply(x, y):
    """Returns the product of x and y"""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y with division by zero handling"""
    if y == 0:
        raise ValueError("Error: Division by zero is not allowed!")
    return x / y

def get_number_input(prompt):
    """Get and validate numeric input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("🔢  SIMPLE CALCULATOR  🔢".center(50))
    print("="*50)
    print("\nSelect an operation:")
    print("  1. ➕ Addition")
    print("  2. ➖ Subtraction")
    print("  3. ✖️  Multiplication")
    print("  4. ➗ Division")
    print("  5. 🚪 Exit")
    print("="*50)

def calculate(choice, num1, num2):
    """Perform calculation based on user choice"""
    operations = {
        '1': (add, '➕', 'Addition'),
        '2': (subtract, '➖', 'Subtraction'),
        '3': (multiply, '✖️', 'Multiplication'),
        '4': (divide, '➗', 'Division')
    }
    
    if choice in operations:
        func, symbol, name = operations[choice]
        try:
            result = func(num1, num2)
            print(f"\n{'='*50}")
            print(f"📊 Result: {num1} {symbol} {num2} = {result}")
            print(f"{'='*50}")
            return result
        except ValueError as e:
            print(f"\n❌ {e}")
            return None
    else:
        print("\n❌ Invalid choice! Please select 1-5.")
        return None

def main():
    """Main function to run the calculator"""
    print("\n🎉 Welcome to the Simple Calculator! 🎉")
    
    while True:
        display_menu()
        
        choice = input("\n👉 Enter your choice (1-5): ").strip()
        
        if choice == '5':
            print("\n👋 Thank you for using the calculator! Goodbye! 👋\n")
            break
        
        if choice in ['1', '2', '3', '4']:
            # Get numbers from user
            num1 = get_number_input("\n📝 Enter first number: ")
            num2 = get_number_input("📝 Enter second number: ")
            
            # Perform calculation
            calculate(choice, num1, num2)
            
            # Ask if user wants to continue
            continue_calc = input("\n❓ Do you want to perform another calculation? (y/n): ").strip().lower()
            if continue_calc != 'y':
                print("\n👋 Thank you for using the calculator! Goodbye! 👋\n")
                break
        else:
            print("\n❌ Invalid choice! Please select a number between 1-5.")

if __name__ == "__main__":
    main()
