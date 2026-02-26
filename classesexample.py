class CreditCardApplication:
    def __init__(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income


class CreditCardProcessor:
    def process_application(self, application):
        if application.age < 18:
            return "Application Rejected: Applicant must be at least 18 years old."
        elif application.income < 20000:
            return "Application Rejected: Applicant must have an income of at least $20,000."
        else:
            return "Application Approved: Congratulations, you are eligible for a credit card!"
        
if __name__ == "__main__":
    application1 = CreditCardApplication("Alice", 25, 50000)
    application2 = CreditCardApplication("Bob", 17, 30000)
    application3 = CreditCardApplication("Charlie", 30, 15000)

    processor = CreditCardProcessor()
    
    print(processor.process_application(application1))  # Should approve
    print(processor.process_application(application2))  # Should reject due to age
    print(processor.process_application(application3))  # Should reject due to income