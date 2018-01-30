index_keys = open("isbn_keys.txt", 'r')
index_values = open("isbn_values.txt", 'r')

values = []
for valueline in index_values:
    valueline = valueline.strip()
    values.append(valueline)

index = {}
i = 0
for keyline in index_keys:
    keyline = keyline.strip()
    index[keyline] = values[i]
    i += 1

print(index)
index_keys.close()
index_values.close()
