def is_palindrome(word):
    word = word.lower() # 소문자
    word = word.replace(' ', '') # 공백 제거
    return word == word[::-1] # 문자열 비교 # return True/False


print(is_palindrome('noon'))