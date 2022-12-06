from datetime import datetime

host_path = "C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"

website_list=["facebook.com","www.facebook.com","www.instagram.com"]

start_date = datetime(2022,11,19)
end_date = datetime(2022,11,21)
today_date = datetime(datetime.now().year,datetime.now().month,datetime.now().day)

while True:
    if start_date <= today_date < end_date:
        with open(host_path ,'r+') as host_file:
            content = host_file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    host_file.write(redirect+" "+site+"\n")
        print("all sites are blocked")
        break
    else:    # end_date < today_date
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    host_file.write(line)
            host_file.truncate()
        print("all sites unblocked")
        break