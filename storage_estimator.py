storage_gb = float(input("Enter storage in GB: "))

storage_mb = storage_gb * 1024
storage_kb = storage_mb * 1024
storage_bytes = storage_kb * 1024

print("--- Storage Estimate ---")
print(f"Storage in GB: {storage_gb:,.2f}")
print(f"Storage in MB: {storage_mb:,.2f}")
print(f"Storage in KB: {storage_kb:,.2f}")
print(f"Storage in bytes: {storage_bytes:,.0f}")
