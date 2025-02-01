from datetime import datetime

class Bill:
    def __init__(self, due_date, what, account_number, auto_pay, min_payment_due, who, frequency):
        self.due_date = due_date
        self.what = what
        self.account_number = account_number
        self.auto_pay = auto_pay
        self.min_payment_due = min_payment_due
        self.who = who
        self.frequency = frequency
        self.payments = []  # For tracking payments (only applicable for Monthly frequency)

    def add_payment(self, date, amount):
        if self.frequency == "Monthly":
            self.payments.append({"date": date, "amount": amount})
        else:
            print("Payments can only be tracked for Monthly frequency.")

    def __str__(self):
        payment_info = ""
        if self.frequency == "Monthly" and self.payments:
            payment_info = "\n  Payments:"
            for payment in self.payments:
                payment_info += f"\n    Date: {payment['date']}, Amount: ${payment['amount']:.2f}"
        return (f"Due Date: {self.due_date}, What: {self.what}, Account Number: {self.account_number}, "
                f"Auto Pay: {self.auto_pay}, Min Payment Due: ${self.min_payment_due:.2f}, "
                f"Who: {self.who}, Frequency: {self.frequency}{payment_info}")

class BillTracker:
    def __init__(self):
        self.bills = []

    def add_bill(self):
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        what = input("Enter What (whom is owed money): ")
        account_number = input("Enter Account Number: ")
        auto_pay = input("Enter Auto Pay (Yes/No): ").capitalize()
        min_payment_due = float(input("Enter Minimum Payment Due ($0.00): "))
        who = input("Enter Who (which account it is from): ")
        frequency = input("Enter Frequency (Monthly/Single): ").capitalize()

        bill = Bill(due_date, what, account_number, auto_pay, min_payment_due, who, frequency)
        self.bills.append(bill)
        print("Bill added successfully!")

    def edit_bill(self):
        account_number = input("Enter Account Number of the bill to edit: ")
        for bill in self.bills:
            if bill.account_number == account_number:
                print("Current Bill Details:")
                print(bill)
                bill.due_date = input("Enter new Due Date (YYYY-MM-DD): ")
                bill.what = input("Enter new What (whom is owed money): ")
                bill.auto_pay = input("Enter new Auto Pay (Yes/No): ").capitalize()
                bill.min_payment_due = float(input("Enter new Minimum Payment Due ($0.00): "))
                bill.who = input("Enter new Who (which account it is from): ")
                bill.frequency = input("Enter new Frequency (Monthly/Single): ").capitalize()
                print("Bill updated successfully!")
                return
        print("Bill not found.")

    def delete_bill(self):
        account_number = input("Enter Account Number of the bill to delete: ")
        for bill in self.bills:
            if bill.account_number == account_number:
                self.bills.remove(bill)
                print("Bill deleted successfully!")
                return
        print("Bill not found.")

    def list_bills(self):
        if not self.bills:
            print("No bills to display.")
            return
        sorted_bills = sorted(self.bills, key=lambda x: datetime.strptime(x.due_date, "%Y-%m-%d"))
        for bill in sorted_bills:
            print(bill)

    def track_payment(self):
        account_number = input("Enter Account Number of the bill to track payment: ")
        for bill in self.bills:
            if bill.account_number == account_number:
                if bill.frequency == "Monthly":
                    date = input("Enter Payment Date (YYYY-MM-DD): ")
                    amount = float(input("Enter Payment Amount ($0.00): "))
                    bill.add_payment(date, amount)
                    print("Payment tracked successfully!")
                else:
                    print("Payments can only be tracked for Monthly frequency.")
                return
        print("Bill not found.")

def main():
    tracker = BillTracker()
    while True:
        print("\nBill Tracker Menu:")
        print("1. Add Bill")
        print("2. Edit Bill")
        print("3. Delete Bill")
        print("4. List Bills")
        print("5. Track Payment")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.add_bill()
        elif choice == "2":
            tracker.edit_bill()
        elif choice == "3":
            tracker.delete_bill()
        elif choice == "4":
            tracker.list_bills()
        elif choice == "5":
            tracker.track_payment()
        elif choice == "6":
            print("Exiting Bill Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()