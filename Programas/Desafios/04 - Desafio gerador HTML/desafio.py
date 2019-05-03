
def tag(tag, *args, **kwargs):
  if 'css' in kwargs:
    kwargs['class'] = kwargs.pop('css')
  attrs = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
  inner = ''.join(args)
  return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
  print(
  tag('p',
  tag('span', 'Curso de Python 3, por '),
  tag('strong', 'Thomas', id='jf'),
  tag('span', ' da '),
  tag('strong', 'Cod3r', id='ll'),
  tag('span', '.'),
  css='alert')
  )
