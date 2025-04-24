def calculate_due_amount(total_bill, amount_paid):
    """
    Calculates the customer's due amount after paying a portion of the bill.

    Args:
        total_bill: The total amount of the bill.
        amount_paid: The amount the customer has paid.

    Returns:
        The due amount, or a message if the amount paid exceeds the bill.
    """
    if amount_paid > total_bill:
        return "Amount paid exceeds the total bill."
    else:
        due_amount = total_bill - amount_paid
        return due_amount

# Example usage:
total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

due = calculate_due_amount(total_bill, amount_paid)

if isinstance(due, str): #check if the returned value is a string or a float
    print(due)
else:
    print(f"The due amount is: {due}")