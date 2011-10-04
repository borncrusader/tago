import app
import getopt
import sys
import os

def check_options():
  """processes the command arguments with getopt and quits the app after printing the usage if there is any error. if not, returns the command switches and the respective args in a dict"""
  try:
    opts, args = getopt.getopt(sys.argv[1:], "vhm:aduyi:")
  except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(1)
  if not opts:
    usage()
    sys.exit(1)
  return dict(opts)

def check_version(switches):
  """checks whether version is requested. if yes, print and quit!"""
  if switches.has_key('-v'):
    version()
    sys.exit(0)

def check_help(switches):
  """checks whether help is requested. if yes, print and quit!"""
  if switches.has_key('-h'):
    usage()
    sys.exit(0)

def usage():
  """prints the usage"""
  print "\nusage is "+sys.argv[0]+" [options]"
  print "options are"
  print "  -v        - version"
  print "  -h        - help"
  print "  -i <mp3>  - specify an mp3 file"
  print "  -m <mode> - mode"
  print "     the available modes are"
  print "     1 - you are intending to work on the tags on all files"
  print "         under the current directory and the files are"
  print "         organised as ./artist/album/files.mp3"
  print "     2 - work on tags for files under the current directory"
  print "         organised as ./album/files.mp3"
  print "     3 - work on tags for files under the current directory"
  print "         organised as ./files.mp3"
  print "   if an mp3 file is specified as an argument, then the modes"
  print "   don't matter and tago will work on the tags only on the file"
  print "  -a        - this is valid for the second mode, when present,"
  print "              . = artist folder"
  print "              can also be used with the -i option for a file"
  print "              in which case, .. == artist folder"
  print "              and . = album folder"
  print "              if not given, tago'll prompt you for the fields"
  print "  -d        - delete tags for the specified file or all files"
  print "              as specified by the mode"
  print "  -u        - set the tag"
  print "  -y        - force yes"

def version():
  """prints the version"""
  print "tago v0.0.1\nAuthor : Srinath Krishna"

def prompt(should_prompt):
  """prompts the user to continue/not if -y option is not given"""
  if should_prompt:
    return True
  else:
    print "Do you like to continue (y/n)? : ",
    yn = raw_input();
    if yn and (yn[0] == 'Y' or yn[0] == 'y'):
      return True
    return False

def check_mp3_file(file_name):
  """checks whether the given file is mp3/MP3"""
  try:
    file_name = file_name.lstrip().rstrip()
    dot_pos = file_name.rindex('.')
    if file_name[dot_pos+1:] == 'mp3' or file_name[dot_pos+1:] == 'MP3': 
      title = os.path.basename(file_name) 
      dot_pos = title.rindex('.')
      title = title[:dot_pos]
      return [True, title]
    else:
      return [False, None]
  except ValueError as err:
     print "incorrect mode with filename : "+file_name
     return [False, None]

def check_prompt_and_delete(file_name, should_prompt):
  """checks file, prompts user and deletes the tags accordingly"""
  [cmd, title] = check_mp3_file(file_name)
  if cmd:
    print 'deleting tags : %s' %(file_name)
    if prompt(should_prompt):
      app.delete_tags(file_name)
  else:
    print "filename ERROR : "+file_name

def check_prompt_and_update(file_name, should_prompt, artist, album):
  """checks file, prompts user and deletes the tags accordingly"""
  [cmd, title] = check_mp3_file(file_name)
  if cmd:
    print 'updating tags : %s, %s, %s, %s' %(file_name, artist, album, title)
    if prompt(should_prompt):
      app.update_tags(file_name, artist, album, title)
  else:
    print "filename ERROR : "+file_name

def exit_on_err(err_msg):
  print err_msg
  sys.exit(1)
