n = int(input())
lines = [input().strip() for _ in range(n)]

poems = []   # danh sách thể loại
i = 0
while i < n:
    words = len(lines[i].split())
    
    # Nếu là thơ thất ngôn tứ tuyệt
    if words == 7:
        # lấy 4 câu
        block = lines[i:i+4]
        if all(len(x.split()) == 7 for x in block):
            poems.append(2)  # thể thơ 2
            i += 4
            continue
    
    # Ngược lại, là thơ lục bát
    # gom các cặp 6-8 liên tiếp
    while i < n-1 and len(lines[i].split()) == 6 and len(lines[i+1].split()) == 8:
        i += 2
    poems.append(1)

# Xuất kết quả
print(len(poems))
for t in poems:
    print(t)
