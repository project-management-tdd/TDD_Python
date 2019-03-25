import unittest
import main

testingList = main.UsersList(main.list)
testingUser = main.User("Sergey", "Aronov", "male", "26", "050")


class TestFindMatching(unittest.TestCase):
    def test_that_matching_gender_not_equal_to_mine(self):
        mine_gender = testingUser.gender
        if(testingList.find_matching(testingUser)):
            self.assertNotEqual(mine_gender, (testingList.find_matching(testingUser)).gender)



if __name__ == '__main__':
    unittest.main()