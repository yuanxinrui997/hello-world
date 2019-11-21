p=[3,5,5,7,7]
name=["原味冰奶茶","香蕉冰奶茶","草莓冰奶茶","蒟蒻冰奶茶","珍珠冰奶茶"]
while 1:
    print("小象奶茶馆开业了\n1）原味冰奶茶 3元\n2）香蕉冰奶茶 5元\n3）草莓冰奶茶 5元\n4）蒟蒻冰奶茶 7元\n5)珍珠冰奶茶 7元\n请输入要购买的序号")
    a=int(input())
    if a<1 or a>5:
        print("Woops!  我们只售卖以上五种奶茶哦！新口味请期待")
        break
    else:
        print("请输入购买数量")
        num=input()
    print("您是否为本店会员？y/n")
    vip=input()
    if vip=="y":
        price=p[a-1]*int(num)*0.9
    elif vip=="n":
        price=p[a-1]*int(num)
    print(name[a-1])
    print("购买数量",'%d'%int(num),"份")
    print("价格为",'%d'%price,"元")
    break
