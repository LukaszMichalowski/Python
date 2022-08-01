cargo=[40,20,4,5,30,8,2,7,3,19,32,40,20,45,15,32,9]
cargo.sort()
cargo.reverse()

prinT("The cargo list is:",cargo)

boxCapacity=90
box=[]
i=0

while i<len(cargo) and (boxCapacity- sum(box) >= min(cargo):               
    if(boxCapacity - sum(box))> =cargo[i]
    box.append(cargo[i])
    i+=1
                      
print("The collected items sums is:",sum(box))
print("The elements are:",box)
