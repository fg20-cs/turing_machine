abc = "ABCÇDEƏFGĞHXIİJKQLMNOÖPRSŞTUÜVYZ"
abc_noS = "ABCÇDEƏFGĞHXIİJKQLMNOÖPRŞTUÜVYZ"
abc_noH = "ABCÇDEƏFGĞXIİJKQLMNOÖPRŞTUÜVYZ"
file_name = "TM_code.txt"

def state(navigation, stateNum, file):
  for letter in abc:
    print("s"+stateNum+","+letter, file=file)
    print("s"+stateNum+","+letter+","+navigation, file = file)
    print("", file = file)

def s_s_noH(navigation, stateF, stateT, file):
  for letter in abc_noH:
    print("s" + stateF + "," + letter, file=file)
    print("s" + stateT + "," + letter + "," + navigation, file = file)
    print("", file = file)

def s_s_no_S_to_lower(navigation, stateF, stateT,i, file):
  print("s"+stateF+','+abc_noS[i-1], file = file)
  print("s"+stateT+","+abc_noS[i-1].lower()+","+navigation, file=file)
  print("", file=file)

def s_s_one_condition(navigation, con1, con2, stateF, stateT,file):
  print("s"+stateF + "," + con1, file=file)
  print("s"+stateT + "," + con2 + "," + navigation, file=file)
  print("", file=file)

def space_to_letter(navigation, stateF, stateT,i, file):
  print("s"+stateF + "," + "_", file=file)
  print("s"+stateT + "," + abc_noS[i-1] + "," + navigation, file=file)
  print("", file=file)

def lower_to_space_noS(navigation, stateF, stateT,i, file):
  print("s"+stateF+','+abc_noS[i-1].lower(), file = file)
  print("s"+stateT+","+"_"+","+navigation, file=file)
  print("", file=file)


#TU machine starts

with open(file_name, "w") as file:

  state(">", "0", file)
  s_s_one_condition("<", "_", "*", "0", "1", file)
  state("<", "1", file)
  s_s_one_condition(">", "_", "_", "1", "2", file)
  for i in range(1,len(abc)):
    s_s_no_S_to_lower(">","2","3a"+str(i),i, file)
    state(">","3a"+str(i),file)
    s_s_one_condition(">", "*", "*", "3a"+str(i), "3b"+str(i), file)
    state(">", "3b"+str(i), file)
    space_to_letter("<", "3b"+str(i), "3c"+str(i),i, file)
    state("<", "3c"+str(i), file)
    s_s_one_condition("<", "*", "*", "3c"+str(i), "3d"+str(i), file)
    state("<", "3d"+str(i), file)
    lower_to_space_noS(">", "3d"+str(i), "2", i, file)

  s_s_one_condition(">", "S", "s", "2", "4", file)
  s_s_noH(">", "4", "4a", file)
  state(">", "4a", file)
  s_s_one_condition(">", "*", "*", "4a", "4b", file)
  state(">", "4b", file)
  s_s_one_condition("<", "_", "S", "4b", "4c", file)
  state("<", "4c", file)
  s_s_one_condition("<", "*", "*", "4c", "4d", file)
  state("<", "4d", file)
  s_s_one_condition(">", "s", "_", "4d", "2", file)

  s_s_one_condition(">", "H", "h", "4", "5a", file)
  state(">", "5a", file)
  s_s_one_condition(">", "*", "*", "5a", "5b", file)
  state(">", "5b", file)
  s_s_one_condition("<", "_", "Ş", "5b", "5c", file)
  state("<", "5c", file)
  s_s_one_condition("<", "*", "*", "5c", "5d", file)
  state("<", "5d", file)
  s_s_one_condition("<", "h", "h", "5d", "5e", file)
  s_s_one_condition(">", "s", "_", "5e", "5f", file)
  s_s_one_condition(">", "h", "_", "5f", "2", file)

  s_s_one_condition(">", "*", "_", "2", "Accept", file)