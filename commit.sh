git show --summary | awk '{print $2}' >commit.txt
sed -n -e '1p'  commit.txt > newcommit.txt 
rm commit.txt
