import whois

info = input("Enter Domain Name: ")
print("Fetching Details....")
try: 
    domain_info = whois.whois(info)
    domain = domain_info.get("domain_name")
    creation = domain_info.get("creation_date")
    updation = domain_info.get("updated_date")
    expiry = domain_info.get("expiration_date")
    server = domain_info.get("name_servers")
    email = domain_info.get("emails")

    print("========================\n"
    "WHOIS Lookup Result\n"
    "========================\n"
    f"Domain Name:   {domain}\n"
    f"Creation On:   {creation}\n"
    f"Updated On:   {updation}\n"
    f"Expired On:   {expiry}\n"
    f"Name Servers:")
    if server:
       for i in server:
          print("-",i)
    else:
        print("No Name Servers found.")

    print("Emails: ")
    if email:
        for i in email:
            print("~",i)
    else:
        print("No Emails found.")
    
    for field in ["name","org","address","city","state","registrant_postal_code","country"]:
        value = domain_info.get(field)
        if value:
            print(f"{field.title()}:    {value}")
except:
    print("This domain does not exist.")