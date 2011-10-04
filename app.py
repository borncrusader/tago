import eyeD3
import utils
import sys
import os

def engine(switches):
  """main engine loop"""
  if switches.has_key('-i'):
    # single file mode
    file_name = switches['-i']
    if os.path.exists(file_name) and os.path.isfile(file_name):
      if switches.has_key('-d'):
        utils.check_prompt_and_delete(switches['-i'], switches.has_key('-y'))
      if switches.has_key('-u'):
        if switches.has_key('-a'):
          try:
            offset = dir.rindex('/')
            album = dir[offset+1:]
          except ValueError as err:
            album = None
          dir = dir[:dir.rfind('/')]
          try:
            offset = dir.rindex('/')
            artist = dir[offset+1:]
          except ValueError as err:
            artist = None
        else:
          artist = None
          album = None
        utils.check_prompt_and_update(switches['-i'], switches.has_key('-y'), artist, album)
    else:
      utils.exit_on_err("filename ERROR : "+file_name)

  else:
    # batch mode
    if switches.has_key('-m'):
      if switches['-m'] == '1':
        for i in os.listdir('.'):
          if os.path.isdir(i):
            artist = i
            os.chdir(i)
            for j in os.listdir('.'):
              if os.path.isdir(j):
                album = j
                os.chdir(j)
                for k in os.listdir('.'):
                  if os.path.isfile(k):
                    if switches.has_key('-d'):
                      utils.check_prompt_and_delete(k, switches.has_key('-y'))
                    if switches.has_key('-u'):
                      utils.check_prompt_and_update(k, switches.has_key('-y'), artist, album)
                os.chdir('..')
            os.chdir('..')
      elif switches['-m'] == '2':
        if switches.has_key('-a'):
          dir = os.getcwd()
          offset = dir.rindex('/')
          artist = dir[offset+1:]
        else:
          artist = None
        for i in os.listdir('.'):
          if os.path.isdir(i):
            album = i
            os.chdir(i)
            for j in os.listdir('.'):
              if os.path.isfile(j):
                if switches.has_key('-d'):
                  utils.check_prompt_and_delete(j, switches.has_key('-y'))
                if switches.has_key('-u'):
                  utils.check_prompt_and_update(j, switches.has_key('-y'), artist, album)
            os.chdir('..')
      elif switches['-m'] == '3':
        if switches.has_key('-a'):
          dir = os.getcwd()
          offset = dir.rindex('/')
          album = dir[offset+1:]
          dir = dir[:offset]
          artist = dir[dir.rfind('/')+1:]
        else:
          artist = None
          album = None
        for i in os.listdir('.'):
          if os.path.isfile(i):
            if switches.has_key('-d'):
              utils.check_prompt_and_delete(i, switches.has_key('-y'))
            if switches.has_key('-u'):
              utils.check_prompt_and_update(i, switches.has_key('-y'), artist, album)
      else:
        exit_on_err('incorrect mode!')

def delete_tags(file_name):
  """deletes the tags on the file specified"""
  cmd = 'eyeD3 --remove-all "%s"' % (file_name)
  print cmd
  os.system(cmd)

def update_tags(file_name, artist, album, title):
  cmd = 'eyeD3 --v2 '
  if artist:
    cmd += '-a "%s" ' %(artist)
  if album:
    cmd += '-A "%s" ' %(album)
  if title:
    cmd += '-t "%s" ' %(title)
  cmd += '"%s"' %(file_name)
  print cmd
  os.system(cmd)
