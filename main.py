import whois

target = input("Enter Domain Name: ")
print("Fetching Details....")

def normalize(value):
        if isinstance(value,list):
            value = value[0]
        return value

try: 
    domain_info = whois.whois(target)
    domain = normalize(domain_info.get("domain_name"))
    creation = normalize(domain_info.get("creation_date"))
    updation = normalize(domain_info.get("updated_date"))
    expiry = normalize(domain_info.get("expiration_date"))
    name_server = domain_info.get("name_servers")
    emails = domain_info.get("emails")

    print("========================\n"
    "WHOIS Lookup Result\n"
    "========================\n"
    f"Domain Name:    {domain}\n"
    f"Creation On:    {creation}\n"
    f"Updated On:     {updation}\n"
    f"Expired On:     {expiry}\n"
    f"Name Servers:")
    if name_server:
        if isinstance(name_server,list):  
            for i in name_server:
                print("-",i)
        else:
            print(name_server)
    else:
        print("No Name Servers found.")

    if emails:
        print("Emails: ")
        if isinstance(emails,list):
            for email in emails:
                print("~",email)
        else:
            print("~",emails)
    else:
        print("No Emails found.")
    
    for field in ["name","org","address","city","state","registrant_postal_code","country"]:
        value = domain_info.get(field)
        if value:
            print(f"{field.title()}:    {value}")
except Exception as e:
    print(f"Error: {e}")