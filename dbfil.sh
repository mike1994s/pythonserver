#!/bin/bash 
for i in `seq 1 100`;
do
    /usr/bin/mysql -uroot -e "INSERT INTO answer_db.question_post (title, text,  author_id) VALUES ('title$i', 'query_post_text$i',  '1');"
done  
