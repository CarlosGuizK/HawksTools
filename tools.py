# Coding with utf-8
import base64
import socket
from time import sleep
import os


os.system('mode con: cols=100 lines=40')

print("""
\n\n
        ██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
        ██║  ██║██╔══██╗██║    ██║██║ ██╔╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
        ███████║███████║██║ █╗ ██║█████╔╝ ███████╗       ██║   ██║   ██║██║   ██║██║     ███████╗
        ██╔══██║██╔══██║██║███╗██║██╔═██╗ ╚════██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
        ██║  ██║██║  ██║╚███╔███╔╝██║  ██╗███████║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
        ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                                                                                                                                                                                                                          
\033[1m By.SidHawks \033[0m                                                                                                                                            
                                           -ohhhhyyyyyssoo+/:-.`                                    
                           ``.--://++oossyyyhdMMMMMMMmyssyhdmNMMmhs+-`                              
                        `-+hNMMMMMMMmhysoo+///:::------.      `-/ohNMMds/.`                         
                    ``.:/+oshNMMMMMNNho:.                           ./ymMMNdyo/:...``               
            .-/+sydmNMMMMMMNmhyo/-.`                 .:/+osyso/:` .`    ./shmNMMMMMM+               
     `/+shmNMMMMMMMMMNmys+-.`                              ./yNMMNhm+`         :dMMMs/.             
      :dMMMMMMMMMdyo:-.````````   `````..-:/:-.`           .:/oMMNsoNNho/:::+smmhddmNMMmy/.         
        :hMMMMMMNs-.....-..``...-:+syhys+:.                  `-omM+-NMyhyMMMdyso+++++oshmMMd+`      
          .sNMMMMMNy/----.--/shmNdy+-`                           :ho+os-oMMh+shhs++++++++ohMMh      
            `/hMMMMMMNy+ohmMMds/-.`   ``````                       .--:/smd++++++++++++++++mMM-     
              `-hMMMMMMMMNh+---.```..--....-:+ossso/:-..`             -sNy++osyhhddhys+++++yMM/     
           .ohNMMMMMMMNh+----...-------+shmNhs/.`  ````       `...-/sddyoydNMMMMMMMMMMNs+++hMM:     
            -smMMMMMMMmo-----------/sdMMms/-.``..--..`...-:::::/hMhso+sdMMMNNMNo/:/omMMh++sNMy`     
               -omMMMMMMMdo/----/yNMMNy:--...-----.-/shmNmhyhmNMMMMy++dMMMMsyMm`    oMNosdMNo`      
                  .+yNMMMMMMNdydMMMNo-----------:sdMMmy/:smMMMMMMMMMmo+yNMMmohMh`  +MMNNMdo.        
                     `-+ymMMMMMMMNs-----------/hMMMd+--yMMMNs/-..-oNMMdooyNMNshMy` `.--.`           
                       .sNMMMMMMMy:----------yMMMN+---dMMMM/       `+dMMmyosdmodM/                  
                       -smMMMMMMMMMds+------yMMMMy/---MMMMMs          -odMMNdyshMy                  
                         `-ohNMMMMMMMMMNdhssMMMMMMMNmmMMMMMM/            `:oymNMMy                  
                             `:ohmMMMMMMMMMMMMMMMMMMMMMMMMMMN-                `.-.                  
                                  `:+shdNMMMMMMMMdoyhdddhso:`                                       
                                         `.--:///-                                                  
""")

choice = int(input(""" 
------ Choice one ------
[1] - To encrypt/decrypt b64
[2] - Port Scan
[3] - Local Server
Your choice : """))

if choice == 1:
    session = int(input("[1]Encrypt "
                        "[2]Decrypt: "))

    if session == 2 :
        string = input('Type text you want decode: ')
        string = string.encode('utf-8')
        print('Converting...'), sleep(0.5)
        encoded = base64.b64decode(string)
        convert = encoded.decode("utf-8")
        print('Your code is : ', convert)

    elif session == 1 :
        encrypt = input('Type phrase or word to encrypt(Base64) : ')
        encrypt = encrypt.encode('utf-8')
        print('Converting...'), sleep(0.5)
        encoded2 = base64.b64encode(encrypt)
        convert2 = encoded2.decode("utf-8")
        print('Your code is : ', convert2)

elif choice == 2:
    print("--- Port scan ---")
    ip = input("Ip address: ")
    portRange = int(input("Range of ports that you want scan: "))
    sleep(1)
    print('Scanning... Wait i tell you the ports open')

    for port in range(1, portRange):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        verify = s.connect_ex((ip, port))
        if verify == 0 :
            recives = print("Port %s open !!!!!!!"%port)


elif choice == 3:
    import http.server
    import socketserver
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(hostname)
    print(local_ip)
    print("\nThe server starts in local of this file")
    print("Warning! If you are using Windows and in it have some virtual machine installed this script not work.\n"
          "So to resolve you have that disable VM network adapter. ")
    PORT = int((input("Type a port to open server: ")))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server starts in port -", PORT)
        print("http://{}:{}/".format(local_ip, PORT))
        httpd.serve_forever()


# If you edit this code quote me