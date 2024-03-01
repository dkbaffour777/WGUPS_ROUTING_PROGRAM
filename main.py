from Models.HashTable import HashTable
from HelperMethods.loadPackageData import loadPackageData
# from HelperMethods.printHashTableData import printHashTableData

# Create a HashTable with a size of 40 (you may adjust the size as needed)
hash_table = HashTable(40)

# Load package data into the hash table
loadPackageData(hash_table)

# This function is used to verify the package CSV file data was successfully loaded into the hash table
# printHashTableData(hash_table)