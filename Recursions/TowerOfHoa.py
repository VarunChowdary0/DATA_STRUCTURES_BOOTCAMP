def TOH(m,src,dst,aux):
    if m <= 0:
        return
    TOH(m-1,src,aux,dst)
    print("Move :"+f"{src} --> {dst}")
    TOH(m-1,aux,dst,src)
src , dst , aux = 'A' , 'B' ,'C'
n = int(input(">> "))
TOH(n,src,dst,aux)