#model star pattensum 1:
a=int(input("Enter the number:"))
for i in range(1,a+1,1):
    st='*'*i
    print(st)
#model star patten sum 2:
a=int(input("Enter the number:"))
for i in range(1,a+1,1):
    st='*'*i
    st=st.rjust(a)
    print(st)
    
   