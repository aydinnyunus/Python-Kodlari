def generate_pascal(height, rows=[]):
    rows.append([1])
    row=[1]
    for i in range(height):
        last = 0
        next_row = []
        for n in row:
            next_row.append(last + n)
            last = n
        next_row.append(1)
        
        row = next_row
        rows.append(row)
    
    return rows

for i in generate_pascal(5):
    print (i)
