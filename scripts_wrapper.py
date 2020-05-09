import os

def main():
  flag = True

  while flag:
    print("Choose an option - ")
    print("  1. Dump mongoDB ")
    print("  2. Restore mongoDB from the folder at ./mongo_dump/job-scheduler")
    try:
      usr_input = int(input())
    except ValueError:
      print("Wrong option selected")
      continue

    if usr_input == 1:
      print("Running script scripts/db_dump.sh to dump mongoDB data")
      os.system("sh scripts/db_dump.sh")
      flag = False
    elif usr_input == 2:
      print("Running script scripts/db_restore.sh to dump mongoDB data")
      os.system("sh scripts/db_restore.sh")
      flag = False
    else:
      continue

if __name__ == "__main__":
    main()
