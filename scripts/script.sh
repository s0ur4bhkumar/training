# !/bin/bash

Date=$(date +%F)
LogFile='/home/sourabh/work/logs/backup.logs'
dest='/home/sourabh/work/archives'
backup='/home/sourabh/work/projects'

echo "Enter the number of files to be kept"

read n_files

log_message(){

  echo "$(date '+%Y-%m-%d %H:%M:%S') [$1] $2" >> "$LogFile"
}


for f in "$backup"/*;
do 
  name=$(basename $f)
  tar -czvf $dest/"$name-$Date".tar.gz $f
  log_message "INFO" "backup created for $name"
done

total_projects=$(find ""$backup/* -maxdepth 0 -type d | wc -l)
echo "total_projects: $total_projects"
echo "files to be kept: $n_files"

a=0
while [ $a -le $((total_projects - n_files)) ];
do
    echo $a
    ((a++))
done
