#linierList([],[]).
#linierList(H, [H]):- not(is_list(H)).
#linierList([H|T],Z):- linierList(H,X),linierList(T,Y),append(X,Y,Z).
import random
 
def list1():
    while True:
        try:
            length_list=input("Masukkan panjang daftar acak yang ingin Anda buat: ")
            range_list=input("Masukkan rande yang Anda inginkan angka yang akan diambil dari: 0-")
            List = random.sample(range(range_list),length_list)
            x=len(List)-2
            print ("Nilai akhir tetapi satu dalam daftar adalah: "+str(List[x]))
            print ("Daftar yang dibuat adalah: "+str(List))
            break
        except ValueError:
            print("Kisaran Anda harus lebih besar dari panjang Anda. Silakan coba lagi.")
        except NameError:
            print("Pastikan Anda mengetikkan bilangan bulat. Coba lagi.")
        except TypeError:
            print("Pastikan Anda mengetikkan angka integer.")
        except SyntaxError:
            print("Silakan ketik nomor integer. Coba lagi.")
list1()