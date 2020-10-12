

Copy book app to blog app....

- copy the book app folder to blog

- rename files and sed contents as below..

- delete migration in blog

- make migrations

- migrate


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@  
#@  find files replace string sed
#@  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   2020-10-11[Oct-Sun]22-19PM 

https://unix.stackexchange.com/questions/112023/how-can-i-replace-a-string-in-a-files


find . -type f -exec sed -i 's/foo/bar/g' {} +


django book app


 grep -rin book
  grep -rin blog


find . -type f -exec sed -i 's/Author/Blog/g' {} +
find . -type f -exec sed -i 's/author/blog/g' {} +

find . -type f -exec sed -i 's/Book/Blog/g' {} +
find . -type f -exec sed -i 's/book/blog/g' {} +


#You Have to rename folder book to blog first.
#
# works.. find files named in . loop through list from a file. rename files named
tmf=/tmp/tmpflist.txt
find . -type f   >$tmf
while read F  ; do
  # replaces first match. not perfect, but does most of them..
  #   newn=$(echo "$F" | sed "s:${basen}:${adn}${basen}:") 
  # replaces last occurence..
  newn=$(echo "$F" | sed -e "s:book:blog:g") 
  echo $newn
  mv "$F" "$newn"
done <$tmf


