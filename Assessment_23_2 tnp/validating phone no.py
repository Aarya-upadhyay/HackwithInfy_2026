def check_validating_phno(s):
   """ if (s.startswith('9') or s.startswith('7') or s.startswith('8')) and len(s)==10 and s.isdigit():
        return "YES"
    return "NO"""
  if re.match(r"^[789]\d{9}$",s):
     return "YES"
  else:
    return "NO"
N=int(input())
for _ in range(N):
    print(check_validating_phno(input()))
