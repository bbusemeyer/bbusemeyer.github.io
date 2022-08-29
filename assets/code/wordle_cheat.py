from collections import defaultdict

def main():
  '''Command-line usage.'''

  accepted = list_options("th***t", ('s','i'))

  print(accepted)

def list_options(pattern, contains=()):
  '''List all words with the pattern, which also contain letters of contains.'''

  with open("scrabble.txt", 'r') as inpf:
    candidates = inpf.read().split('\n')

  wantlen = len(pattern)
  checks = dissect_pattern(pattern)

  accepted = set(check_word(word.lower(), wantlen, checks, contains) for word in candidates)
  accepted.remove('')

  return accepted

def check_word(word, wantlen, checks, contains):

  if len(word) != wantlen:
    return ''

  for check in checks:

    if word[check] != checks[check]:
      return ''

  for has in contains:
    if not has in word:
      return ''

  return word

def dissect_pattern(pattern):
  req = {}
  for ix, c in enumerate(pattern):
    if c != '*':
      req[ix] = c
  return req

if __name__=='__main__':
  main()
