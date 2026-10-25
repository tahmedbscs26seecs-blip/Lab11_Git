storage_gb = float(input("Enter storage in GB: "))

storage_mb = storage_gb * 1024
storage_kb = storage_mb * 1024
storage_bytes = storage_kb * 1024

print("Storage in MB: ", storage_mb)
print("Storage in KB: ", storage_kb)
print("Storage in bytes: ", storage_bytes)
