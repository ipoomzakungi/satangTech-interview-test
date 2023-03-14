import unittest

class Bank(list):

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > len(self) or account2 < 1 or account2 > len(self) or money > self[account1-1]:
            return False
        self[account1-1] -= money
        self[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > len(self):
            return False
        self[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > len(self) or money > self[account-1]:
            return False
        self[account-1] -= money
        return True
    


class TestBank(unittest.TestCase):
    
    def test_basic_transactions(self):
        bank = Bank([10, 100, 20, 50, 30]) #[10, 100, 20, 50, 30]
        
        self.assertTrue(bank.withdraw(3, 10))
        self.assertEqual(bank, [10, 100, 10, 50, 30]) #[10, 100, 10, 50, 30]
        
        self.assertTrue(bank.transfer(5, 1, 20))
        self.assertEqual(bank, [30, 100, 10, 50, 10]) #[30, 100, 10, 50, 10]
        
        self.assertTrue(bank.deposit(5, 20))
        self.assertEqual(bank, [30, 100, 10, 50, 30]) #[30, 100, 10, 50, 30]
        
        
    def test_invalid_transactions(self):
        bank = Bank([10, 100, 20, 50, 30])
        
        self.assertFalse(bank.withdraw(3, 30))
        self.assertEqual(bank, [10, 100, 20, 50, 30])
        
        self.assertFalse(bank.transfer(5, 1, 40))
        self.assertEqual(bank, [10, 100, 20, 50, 30])
        
        
        


if __name__ == '__main__':
    unittest.main()