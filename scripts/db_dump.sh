#!/bin/bash
source scripts/constants.sh


echol "${LCYAN}This script will dump the changes you made to DB online-exam in mongo".
echol "${LCYAN}The data is dumped at the <parent_folder>/mongo_dump/"
echol "${LCYAN}It's always recommended to dump the DB before you push the changes${NC}\n\n"

echol "${YELLOW}Checking the mongoDB status...."

if pgrep -x "mongod" > /dev/null
then
    echol "${GREEN}MongoDB is running with PID ${NC} `pgrep mongod`"
    echol "${GREEN}Preparing to dump the the database ..."

    mongodump --db=online-exam --out=mongo_dump
    echol "${GREEN}Dump complete ..."
    echol "${RED}Exiting the script now..."
else
    echol "${RED}MongoDB is not running. Please ensure the mongoDB is running before triggering this script."
    echol "${RED}Exiting the script now..."
    exit 1
fi
