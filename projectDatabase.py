import sqlite3
db = sqlite3.connect('jomaiya.db')
db.execute('drop table if exists somaiya')
db.execute('create table somaiya(i int,amin text, class text, section text)')
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('01','rina','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('02','kira','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('03','jira','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('04','tina','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('05','riya','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('06','muna','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('07','nuha','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('08','luna','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('09','kina','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('10','samiya','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('11','piho','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('12','ekra','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('14','gfds','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class ,section ) values(?,?,?,?)',('15','shsd','nine','girl'))
db.execute('insert into somaiya (i ,amin ,class,section ) values(?,?,?,?)',('16','fhdhf','nine','girl'))

db.commit()
select = db.execute('select * from somaiya')
for row in select:
    print(row)