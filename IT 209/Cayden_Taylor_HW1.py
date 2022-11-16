#-------------------------------------------------------------------------------
# HW1
# Student Name: Cayden Taylor
# Submission Date: 06/16/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: Session 2 sample codes, session 3 sample codes, lab 2, lab 3
#-------------------------------------------------------------------------------
# Notes to grader: fully implemented
#-------------------------------------------------------------------------------

class URL(object):
    valid_protocol = ["HTTP", "HTTPS", "FTP", "http", "https", "ftp"] #initializing the valid tld's and protocols
    valid_tld = [".com", ".net", ".org", ".edu"]
    secured = ["HTTPS", "https"]

    def __init__(self, protocol, subdomain, domain, top_level_domain, path): #init
        self.protocol = protocol
        self.subdomain = subdomain
        self.domain = domain
        self.top_level_domain = top_level_domain
        self.path = path

    def get_full_domain_address(self): #full domain name
        return "//{}.{}{}/".format(self.subdomain, self.domain, self.top_level_domain)

    def get_full_address(self):#full website name
         return "{}://{}.{}{}/{}".format(self.protocol, self.subdomain, self.domain, self.top_level_domain, self.path)
        
    def is_url_valid(self): #if else for boolean operator output
        if self.protocol in self.valid_protocol and self.top_level_domain in self.valid_tld:
            return True
        else:
            return False
         

    def is_secured(self): #if else for boolean operator output to find out if secured 
        if self.protocol in self.secured:
            return True
        else:
            return False
          

    def __str__(self):#formats the string to put in info from file into correct category
        protocol_str = "\nProtocol: {}".format(self.protocol)
        
        subdomain_str = "Subdomain: {}".format(self.subdomain)
        domain_str = "Domain: {}".format(self.domain)
        top_level_domain_str = "Top Level Domain: {}".format(self.top_level_domain)
        
        path_str = "Path: {}".format(self.path)
        full_address_str = "Full Address: {}".format(self.get_full_address())
        is_url_valid_str = "Valid: " + str(self.is_url_valid())
        is_secured_str = "Secured: " +str(self.is_secured())
        

        return protocol_str + "\n" + subdomain_str + "\n" + domain_str + "\n" + top_level_domain_str + "\n" + path_str + "\n" + full_address_str + "\n" + is_url_valid_str + "\n" + is_secured_str
        #formatted to return similiar to rubric


def main():
    file = ('HW1_Readfile.txt') #opening the .txt file
    for url in open(file, 'r'): #loop for multiple url links
        formatted_url = url.strip("\n").split("/")#formats to split info up
        formatted_url[2] = formatted_url[2].split(".")
        
        protocol = formatted_url[0][:-1]#slicing to get only neccesary info
        sub_domain = formatted_url[2][0]
        domain = formatted_url[2][1]
        top_level_domain = formatted_url[2][-1]
        top_level_domain = "."+top_level_domain#adds the '.' to the tld
        path = formatted_url[-1]

        
        print(URL(protocol, sub_domain,domain, top_level_domain, path))
        print("********************************************************")



main()
        














        
        
        
        
        
