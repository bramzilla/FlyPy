from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Generate random data
name = fake.name()
address = fake.address()
email = fake.email()
phone_number = fake.phone_number()
date_of_birth = fake.date_of_birth()

# Print the generated data
print("Name:", name)
print("Address:", address)
print("Email:", email)
print("Phone Number:", phone_number)
print("Date of Birth:", date_of_birth)