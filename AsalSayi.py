def asalsayi():
    sayi = input("Bir sayi girin: ")
    if sayi.isdigit():
        sayi = int(sayi)
        x = sayi-1

        while x > 1:
            if sayi % x == 0:
                print("{} asal değildir.".format(sayi))
                break
            else:
                x -= 1
        else:
            print("{} asal sayıdır".format(sayi))
    else:
        print("Sayı Hatalı")
        asalsayi()
asalsayi()
