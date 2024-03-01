# This function verifies the package data in the CSV file was loaded into the hash table
def printHashTableData(hash_table):
    for index, bucket in enumerate(hash_table.table):
        if bucket is not None:
            for key, item in bucket:
                print(f"Package ID: {key}")
                print(f"Delivery Street: {item.delivery_street}")
                print(f"Delivery City: {item.delivery_city}")
                print(f"Delivery State: {item.delivery_state}")
                print(f"Delivery Zip Code: {item.delivery_zip}")
                print(f"Delivery Deadline: {item.delivery_deadline}")
                print(f"Package Weight: {item.package_weight}")
                print(f"Delivery Notes: {item.delivery_notes}")
                print(f"Delivery Status: {item.delivery_status}")
                print(f"Time of Departure: {item.time_of_departure}")
                print(f"Time of Delivery: {item.time_of_delivery}")
                print("---")