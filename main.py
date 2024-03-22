stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
allowed = "0123456789Ex.-^"
num_list = []
# Type your code below
for i in stdform:
  if i == "x":
    index = stdform.index("x")

for i in stdform:
  if i in allowed:
    if stdform.count("x") == 1:
        if stdform.count(".") ==1:
            if stdform.index(".") < index:
                for i in stdform:
                    num_list.append(i)
                del num_list[index:index+4]
                num_list.insert(index,"E")
                print(f'This number in E notation is {"".join(num_list)}.')
                break
else:
    print("Error converting to scientific E notation.")