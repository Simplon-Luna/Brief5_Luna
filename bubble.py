table = [18,25,3,14,2,9,1,50]
loop_count = 0
unsorted = 1

while unsorted > 0:
    unsorted = 0
    
    for i in range(len(table)-1):
        loop_count += 1
        compare_a = table[i]
        compare_b = table[i+1]
        print (table)
        
        if compare_a > compare_b:
            unsorted += 1
            table[i] = compare_b
            table[i+1] = compare_a
            print (unsorted)
            
print (loop_count)