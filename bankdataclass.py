from dataclasses import dataclass


@dataclass
class BankAccount:
    account_number: str
    holder_name: str
    balance: float
    account_type: str
    currency: str = "GBP"

    def __post_init__(self):
        if self.balance < 0:
            raise ValueError("Balance cannot be negative")

        if self.account_type not in ("current", "savings", "isa"):
            raise ValueError("account_type must be 'current', 'savings' or 'isa'")

    @property
    def is_overdrawn(self) -> bool:
        return self.balance < 0


acc = BankAccount(
    account_number="GB12345678",
    holder_name="Madhu Sudhanan",
    balance=1500.00,
    account_type="savings"
)

print(acc)
print("Is overdrawn:", acc.is_overdrawn)
