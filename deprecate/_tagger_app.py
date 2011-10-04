import tagger
import utils
import sys
import os

def engine(switches):
  """main engine loop"""
  if switches.has_key('-d'):
    # file deletion mode
    if switches.has_key('-i'):
      # single file mode
      file_name = switches['-i']
      if os.path.exists(file_name):
        utils.check_prompt_and_delete(switches['-i'], switches.has_key('-y'))
      else:
        print "filename ERROR : "+file_name

    else:
      # batch mode
      if switches.has_key('-m'):
        if switches['-m'] == '1':
          print "mode 1 selected"
          for i in os.listdir('.'):
            if os.path.isdir(i):
              os.chdir(i)
              for j in os.listdir('.'):
                if os.path.isdir(j):
                  os.chdir(j)
                  for k in os.listdir('.'):
                    utils.check_prompt_and_delete(k, switches.has_key('-y'))
                  os.chdir('..')
              os.chdir('..')
        elif switches['-m'] == '2':
          print "mode 2 selected"
          for i in os.listdir('.'):
            if os.path.isdir(i):
              os.chdir(i)
              for j in os.listdir('.'):
                utils.check_prompt_and_delete(j, switches.has_key('-y'))
        else:
          print "incorrect mode!"
          utils.usage()
          sys.exit(1)

def delete_tags(file_name):
  """deletes the tags on the file specified"""
  # id3v1 tags
  try:
    mp3_tag = tagger.ID3v1(file_name)
    if mp3_tag.tag_exists():
      mp3_tag.remove_and_commit()
      print "id3v1 tags deleted : "+file_name
  except IOError as err:
    print "id3v1 ERROR : '%s' while processing : %s" %(err, file_name)

  # id3v2 tags
  try:
    mp3_tag = tagger.ID3v2(file_name)
    if mp3_tag.tag_exists():
      # an interim solution. not the best though! find some good solution
      mp3_tag.frames = []
      mp3_tag.commit()
      print "id3v2 tags deleted : "+file_name
  except IOError as err:
    print "id3v2 ERROR : '%s' while processing : %s" %(err, file_name)
