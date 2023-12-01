import re

f = open("sample_2.txt","rt")
fout = open("output_2.txt","wt")

for line in f:
    fout.write(line.replace('oneight','18').replace('twone','21').replace('threeight','38').replace('fiveight','58').replace('sevenine','79').replace('eightwo','82').replace('eighthree','83').replace('nineight','98').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9'))
    
f.close()
fout.close()




f = open("output_2.txt","r")

total = 0

a = f.readlines()

for x in a:
    b = re.findall('\d+', x)
    
    c= int(b[0])
    while c >= 10:
        c = c/10;
    c = int(c)

    d = int(b[len(b)-1]) % 10
    
    cal_number = 10*c + d
    print(cal_number)
    total = total + cal_number
print(total)
