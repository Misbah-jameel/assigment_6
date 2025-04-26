class Bank:
    bank_name = "Mezan Bank"  # class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # class variable change

# Objects banaye
islamic_bank = Bank()
MCB_bank = Bank()

# Pehle bank name print kiya
print(islamic_bank.bank_name)
print(MCB_bank.bank_name)

# Bank ka naam change kia
Bank.change_bank_name("MCB Bank")

# Baad mein phir print kiya
print(islamic_bank.bank_name)
print(MCB_bank.bank_name)
