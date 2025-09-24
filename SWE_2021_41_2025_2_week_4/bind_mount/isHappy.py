def isHappy(n):
    used = []
    while(n > 1):
        if(n in used):
            return False
        used.append(n)
        num = []
        a = n
        while(a >= 10):
            new = a%10
            a = a//10
            num.insert(0,new)
        num.insert(0,a)
        result = 0
        for i in num:
            result += i*i
        n = result

    return True

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")