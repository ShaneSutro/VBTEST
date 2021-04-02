from vestaboard import Formatter

def main(*args, **kwargs):
  fm = Formatter()
  return {'characters': fm.convert('The quick brown fox jumps over the lazy dog!')}


if __name__ == '__main__':
  print(main())
