def generate(n, l = 0, r = 0, answer = ''):
    if l < n:
        answer += '('
        l += 1
        generate(n, l, r, answer)
    if r < l:
        answer += ')'
        r += 1
        generate(n, l, r, answer)
    if len(answer) == 6:
        print(answer)
    return 
if __name__ == "__main__":
    n = 3
    generate(n)