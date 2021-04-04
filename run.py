from vestaboard import Formatter

def main(*args, **kwargs):
  print('Changed args: ', args)
  fm = Formatter()
  return {'characters': fm.convert('ABCDEF')}

if __name__ == '__main__':
  print(main())
