from vestaboard import Formatter

def main(*args, **kwargs):
  fm = Formatter()
  return {'characters': fm.convert('The quick brown fox jumps over the lazy dogs!lll')}

if __name__ == '__main__':
  print(main())
