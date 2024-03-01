from Models.Package import Package

# Function to load package data into the hash table
def loadPackageData(hash_table):
    with open('BootstrapData/packageCSV.csv', 'r') as file:
        # Skip the first line
        next(file)
        for row in file:
            data = row.strip().split(',')
            package_id = int(data[0])
            delivery_street = data[1]
            delivery_city = data[2]
            delivery_state = data[3]
            delivery_zip = data[4]
            delivery_deadline = data[5]
            package_weight = float(data[6])
            delivery_notes = data[7]
            delivery_status = "At the Hub"
            time_of_departure = None
            time_of_delivery = None

            # Create Package object
            package = Package(package_id, delivery_street, delivery_city, delivery_state, delivery_zip, delivery_deadline, package_weight, delivery_notes, delivery_status, time_of_departure, time_of_delivery)
            
            # Insert Package object into HashTable with key=PackageID
            hash_table.insert(package_id, package)