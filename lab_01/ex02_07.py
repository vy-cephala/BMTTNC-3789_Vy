print ("nhap cac dong van ban (nhap 'done' de ket thuc ):")
lines = []
while True:
    line = input ()
    if line.lower () == 'done':
        break 
    lines.append(line)
print ("\cac dong da nhap sau khi chuyen thanh chu in hoa :")
for line in lines:
    print (line.upper())