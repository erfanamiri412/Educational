def is_paindrome(s):
    if s == s[::-1]:
        return 'paindrome'
    else:
        return 'not palindrome'
print(is_paindrome('wow'))

# answer = palindrome