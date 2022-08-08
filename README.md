# softwareone_project
# Shopping cart

It is a partial implementation of a shopping till system, which you might find at a supermarket.
This implementation was done by a Junior developer, you as a Senior Software Engineer have been requested to refactor this project.
You may make any technical decisions you would like, but must not change the given abstract class (abc.ShoppingCart) which is used by the shopping till hardware and cannot be easily updated.
Please treat this code as an element of a larger production system. The code is being refactored to ensure reliability and testability.

Tasks requested:
- Make the receipt print items in the order that they were added
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer
- Be able to fetch product prices from an external source (json file, database ...)
- Be able to display the product prices in different currencies (not only Euro).
- Update the test suite to extend coverage and limit the number of tests which need changing when changes are introduced
- Any other changes which improve the reliability of this code in production

If you do not have enough information, make any assumptions you would like and note them down with TODO comments. Feel free to make comments that highlight completion of the tasks listed above.

Please budget 3 hours to complete, and your code should be production ready, clean and tested! Please ensure the code is version controlled also, and make sure to make several commits with sensile commit messages while working on this. When submitting please either:
- Provide a Github/GitLab/etc. link that we can view and clone your work; or
- Use git-bundle (https://git-scm.com/docs/git-bundle) to create a bundle file and send this to us.

# TODO comments
1) Assumed json_data will be in  following format 
{
    'apple' : 1.0,
    'banana' : 1.1,
    'kiwi' : 3.0,
    'mango' : 5.0
}

2) If product_code not found in json file, we return such price with 0.0

3) You can also set locale currency code to any of currency code in the list locale= ['en_AU.utf8', 'en_BW.utf8', 'en_CA.utf8',  'en_DK.utf8', 'en_GB.utf8', 'en_HK.utf8', 'en_IE.utf8', 'en_IN', 'en_NG','en_PH.utf8', 'en_US.utf8', 'en_ZA.utf8','en_ZW.utf8', 'ja_JP.utf8']


4) We can also fetch prices from database with following approach

We can use python's pymysql library to work with the database. This library provides the programmer the functionality to run MySQL query using Python.

Algorithm:

Step 1: Connect to database using connect() method in pymysql.
Step 2: Get input of price range 
Step 3: Create a query to fetch records of products with price within a given price range. 
query= "select item,price from products" 
Step 4: Execute the query and print the results.

To Run coverage

a) coverage run test_cart.py

b) coverage report -m

c) coverage html