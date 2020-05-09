#!/bin/bash

#    ---------- constant part ----------
NC='\033[0m' # No Color
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
LCYAN='\033[0;36m'
LGRAY='\033[1;30m'

log_prefix(){
  script_name1=`basename $0`
  echo "${LGRAY}[ `date +"%Y/%m/%d %T"` $script_name1 ] ${NC}"
}

echol(){
  echo "$(log_prefix) $1"
}
