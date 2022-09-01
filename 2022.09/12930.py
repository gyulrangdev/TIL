def solution(s):
    return ' '.join([ ''.join([c.upper() if idx%2==0 else c.lower() for idx, c in enumerate(_s)]) for _s in s.split(' ') ])