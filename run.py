from vestaboard import Formatter

def main(*args, **kwargs):
  fm = Formatter()
  return {'characters': fm.convert('ABCDEF')}

if __name__ == '__main__':
  print(main())