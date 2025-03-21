Bill Tracker based on your requirements. This program uses a simple text-based interface
 to manage invoices, including adding, editing, deleting, and listing entries by due date. 
It also includes fields for Due Date, What (whom is owed money), Account Number, Auto Pay,
 Minimum Payment Due, Who (which account it is from), and Frequency (Monthly or Single)
 For monthly invoices, it allows tracking payment dates and amounts.
============================================
Features:

    Add Bill: Add a new bill with all the required fields.

    Edit Bill: Edit an existing bill by providing the account number.

    Delete Bill: Delete a bill by providing the account number.

    List Bills: Display all bills sorted by due date.

    Track Payment: For monthly bills, track payment dates and amounts.

    Exit: Exit the program.
============================================
Example Usage:

    Add a bill:
Enter Due Date (YYYY-MM-DD): 2023-11-15
Enter What (whom is owed money): Electricity Bill
Enter Account Number: 12345
Enter Auto Pay (Yes/No): Yes
Enter Minimum Payment Due ($0.00): 50.00
Enter Who (which account it is from): Bank Account
Enter Frequency (Monthly/Single): Monthly
============================================
Track a payment for a monthly bill:
Enter Account Number of the bill to track payment: 12345
Enter Payment Date (YYYY-MM-DD): 2023-11-10
Enter Payment Amount ($0.00): 50.00
============================================
List all bills:
Due Date: 2023-11-15, What: Electricity Bill, Account Number: 12345,
 Auto Pay: Yes, Min Payment Due: $50.00, Who: Bank Account, Frequency: Monthly
 Payments:
 Date: 2023-11-10, Amount: $50.00
============================================
To use the Bill Tracker app, follow these steps:
-------------------------------------------------------------------
Step 1: Run the Program

    Save the Python code provided in the previous response to a file, e.g., bill_tracker.py.

    Open a terminal or command prompt.

    Navigate to the directory where the file is saved.

    Run the program using the command:

============================================
Open a terminal or command prompt.
python bill_tracker.py

=================================
Step 2: Navigate the Menu

Once the program is running, you'll see a menu with the following options:
Copy

Bill Tracker Menu:
1. Add Bill
2. Edit Bill
3. Delete Bill
4. List Bills
5. Track Payment
6. Exit

To select an option, type the corresponding number and press Enter.
Step 3: Add a Bill

    Select Option 1: Add Bill.

    Enter the details for the bill as prompted:

        Due Date: Enter the due date in YYYY-MM-DD format (e.g., 2023-11-15).

        What: Enter whom the money is owed to (e.g., Electricity Bill).

        Account Number: Enter the account number (e.g., 12345).

        Auto Pay: Enter Yes or No.

        Minimum Payment Due: Enter the amount (e.g., 50.00).

        Who: Enter which account the payment is from (e.g., Bank Account).

        Frequency: Enter Monthly or Single.

    The bill will be added to the tracker.

Step 4: Edit a Bill

    Select Option 2: Edit Bill.

    Enter the Account Number of the bill you want to edit.

    Update the fields as prompted.

    The bill will be updated with the new details.

Step 5: Delete a Bill

    Select Option 3: Delete Bill.

    Enter the Account Number of the bill you want to delete.

    The bill will be removed from the tracker.

Step 6: List All Bills

    Select Option 4: List Bills.

    All bills will be displayed, sorted by Due Date.

    For monthly bills, any tracked payments will also be displayed.

Step 7: Track a Payment

    Select Option 5: Track Payment.

    Enter the Account Number of the bill you want to track a payment for.

    If the bill has a Monthly frequency, you can enter:

        Payment Date: Enter the date in YYYY-MM-DD format.

        Payment Amount: Enter the amount paid (e.g., 50.00).

    The payment will be recorded for that bill.

Step 8: Exit the Program

    Select Option 6: Exit.

    The program will close.

