class User_details:
    def __init__(self, email=None, username=None, domain=None):
        self.email = email
        self.username = username
        self.domain = domain
    
    
    def get_email(self):
        while True:
            print()
            self.email = input("Email: ")

            if "@" not in self.email:
                print("Not an email")
                continue
        
            break
        return self.email
             

    
    def extract_name(self):
        split_email = self.email.strip().split("@", 1)

        self.username = split_email[0]
        return self.username

    
    def extract_domain(self):
        split_email = self.email.strip().split("@", 1)

        self.domain = split_email[-1]
        return self.domain


def return_details(username, domain):
    print("Your username is:", username)
    print("Your domain is:", domain)
    print()

def main():
    User_details()
    email = User_details().get_email()
    username = User_details(email=email).extract_name()
    domain = User_details(email=email).extract_domain()
    return_details(username, domain)

if __name__ == "__main__":
    main()