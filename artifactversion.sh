#!/usr/bin/env sh

function extract_version_without_snapshot(){
   grep version $1 | cut -d= -f2 | cut -d- -f1 

}

function bump_hotfix_version()
{
   major_version=$(echo $1 | cut -d. -f1)
   minor_version=$(echo $1 | cut -d. -f2)
   hotfix_version=$(echo $1 | cut -d. -f3)
   echo "${major_version}.${minor_version}.$(( ${hotfix_version}+1))"
}

function generate_bumped_setup()
{
   current_version=$(extract_version_without_snapshot setup.py)
   new_version=$(bump_hotfix_version $current_version)
   sed "s/version=.*/version=$new_version-SNAPSHOT',/g" setup.py >1.txt
   mv 1.txt setup.py
}
