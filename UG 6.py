from pickle import NONE


class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self,no_rekening,nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def insert_head(self,no,nama,saldo=0):
        baru = NodeTabungan(no,nama,saldo)
        if self.isEmpty()==True:
            self.head = baru
            self.tail = baru
            self.tail.next = None
        else:
            baru.next = self.head
            self.head = baru
        self.size += 1

    def delete(self, position):
        n = self.head
        if position == 0:
            self.head = n.next
            del n
            self.size -= 1
        elif position == self.size-1:
            while n.next != self.tail:
                n = n.next
            del self.tail
            self.tail = n
            self.tail.next = None
            self.size -= 1

        else:
            for i in range(position-1):
                n = n.next
            
            n.next = n.next.next
            del n.next

    # def filter(self,batas):
    #     pass
    
    def update(self,bunga):
        if self.tail == None:
            return
        temp = self.tail
        if bunga <0 and bunga >100:
            print("Maaf besan persen harus diantara 0-100")
        else:
            b = temp.saldo + (temp.saldo * bunga)
            return b

    def printlist(self):
        temp = self.head
        while(temp):
            print("Norek  :""%d " % (temp.no_rekening)),
            print("Nama :",(temp.nama)),
            print("Saldo :""%d " % (temp.saldo)),
            temp = temp.next
        n = self.head
        # while(n):
        print("Rekening yang berhasil di hapus sebanyak : ",(n.next))
        temp = self.tail
        print("Semua saldo di rekening berhasil ditambah sebanyak : ",(self.tail))

list = SLLNC()
list.insert_head(110,"Yudha",150000)
list.printlist()
list.update(200)