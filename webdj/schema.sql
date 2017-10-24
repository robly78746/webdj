drop table if exists users;
create table users (
  id integer primary key autoincrement, 
  username varchar(20) not null unique
);
drop table if exists logins;
create table logins (
  id integer primary key autoincrement,
  username varchar(20) not null unique,
  password varchar(120) not null,
  userid integer not null unique,
  foreign key(userid) references users(id)
);

drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
