class Bank(object):
    
    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self._balance = balance
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        n = len(self)
        if (account1 - 1) >= n or (account2 -1) >= n or self._balance[account1 - 1] < money:
            return False
        
        self._balance[account1 - 1] -= money
        self._balance[account2 - 1] += money
        return True
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if (account - 1) >= len(self):
            return False
        
        self._balance[account - 1] += money
        return True
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if (account - 1) >= len(self) or self._balance[account - 1] < money:
            return False

        self._balance[account - 1] -= money
        return True
    
    def __len__(self):
        """
        :rtype: int
        """
        return len(self._balance)
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10), bank._balance)
print(bank.transfer(5, 1, 20),  bank._balance)
print(bank.deposit(5, 20), bank._balance)
print(bank.transfer(3, 4, 15), bank._balance)
print(bank.withdraw(10, 50), bank._balance)
