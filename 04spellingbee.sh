cd ~/Code/mcb185_homework
ln -s ../MCB185/data/dictionary.gz ./dictionary
gunzip -c dictionary | grep -E "^[rzoncai]{4,}$" | grep "r"