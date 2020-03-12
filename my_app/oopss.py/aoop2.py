class Item():
    def __init__(self,name,code):
        self.name=name
        self.code=code
itemlist=[]
i=1
while i==1:
    print('A.add item\n','B.view item\n','C.view all','D.delete','E.exit')
    choice=input('enter choice-')
    if  choice=='A':
        itemcode=input('add item :')
        itemname=input('add item :')
        obj=Item(itemcode,itemname)
        itemlist.append(obj)
    elif choice=='B':
        print((itemlist[-1]).name)
    elif choice=='C':
        for x in itemlist:
            print(x.name,x.code,sep=" ")
    elif choice=='D':
        itemlist.pop()
    elif choice=='E':
        i=i-1